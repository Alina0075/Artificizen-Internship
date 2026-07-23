from fastapi import APIRouter
from models.schemas import ChatRequest, ChatResponse, Source
from services.embeddings import get_embeddings
from services.qdrant_service import search_chunks
from services.groq_service import generate_answer
from services.history import (
    get_history,
    add_messages
)
from services.cache import (
    get_cached_answer,
    save_cached_answer
)
from fastapi.responses import StreamingResponse
from services.groq_service import (
    generate_answer,
    stream_answer
)


router=APIRouter(tags=['Chat'])
@router.post("/chat",response_model=ChatResponse)
async def chat(request:ChatRequest):
    cached=get_cached_answer(
        request.session_id,
        request.query
    )
    if cached: 
        return ChatResponse(
            answer=cached['answer'],
            sources=[
                Source(
                    filename=source['filename'],
                    chunk_index=source['chunk_index']
                )
                for source in cached['sources']
            ]
        )
    
    query_embedding=get_embeddings(request.query)
    retrived_chunks=search_chunks(query_embedding)
    context="\n\n".join(chunk['text']for chunk in retrived_chunks)
    history=get_history(request.session_id)
    answer=generate_answer(
        context=context,
        query=request.query,
        history=history
    )
    add_messages(
        request.session_id,
        "user",
        request.query
    )
    add_messages(
        request.session_id,
        "assistant",
        answer
    )
    sources=[
        Source(
            filename=chunk['filename'],
            chunk_index=chunk['chunk_index']
        )
        for chunk in retrived_chunks
    ]
    save_cached_answer(
        request.session_id,
        request.query,
        answer,
        [
            {
            "filename":source.filename,
            "chunk_index":source.chunk_index
            } 
            for source in sources
        ]
    )
    return ChatResponse(
        answer=answer,sources=sources)
    
@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    query_embedding = get_embeddings(request.query)

    retrieved_chunks = search_chunks(query_embedding)

    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
    )

    history = get_history(request.session_id)

    generator = stream_answer(
        context=context,
        query=request.query,
        history=history
    )

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )
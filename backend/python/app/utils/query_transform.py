from typing import Tuple

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnablePassthrough


def setup_query_transformation(llm) -> Tuple[Runnable, Runnable]:
    """Setup query rewriting and expansion with async support"""

    # Query rewriting prompt
    query_rewrite_prompt = ChatPromptTemplate.from_template(
        """You are an expert at reformulating search queries to make them more effective.
        Given the original query below, rewrite it to make it more specific and detailed:

        Original Query: {query}

        Rewritten Query:"""
    )

    # Query expansion prompt
    query_expansion_prompt = ChatPromptTemplate.from_template(
        """Generate 2 additional search queries that capture different aspects or perspectives of the original query.
        These should help in retrieving a diverse set of relevant documents.

        Original Query: {query}

        Return only the list of queries, one per line without any numbering:"""
    )

    # Create async-compatible chains
    rewrite_chain = (
        {"query": RunnablePassthrough()}
        | query_rewrite_prompt
        | llm
        | StrOutputParser()
    )

    expansion_chain = (
        {"query": RunnablePassthrough()}
        | query_expansion_prompt
        | llm
        | StrOutputParser()
    )

    return rewrite_chain, expansion_chain


def setup_followup_query_transformation(llm) -> Runnable:
    """Setup query rewriting for follow-up questions based on conversation history."""

    # Use a static variable for the prompt template string to avoid re-allocation
    _QUERY_REWRITE_PROMPT_TEMPLATE = (
        "You are an expert at reformulating search queries to make them more effective.\n"
        "Given the original query below, rewrite it to make it more specific and detailed as per the previous conversations and the follow up question\n"
        "so that it can be used to search for relevant documents:\n\n"
        "Previous Conversations: {previous_conversations}\n"
        "Follow up question: {query}\n\n"
        "Return only the rewritten query, no other text or formatting.\n"
        "Rewritten Query:"
    )

    # Create async-compatible chains

    # Cache ChatPromptTemplate object at the function level if possible
    # This assumes prompt is static and avoids unnecessary re-parsing
    # Using function attribute for thread safety and easy binding
    if not hasattr(setup_followup_query_transformation, "_query_rewrite_prompt"):
        setup_followup_query_transformation._query_rewrite_prompt = (
            ChatPromptTemplate.from_template(_QUERY_REWRITE_PROMPT_TEMPLATE)
        )
    query_rewrite_prompt = setup_followup_query_transformation._query_rewrite_prompt

    # Prebuild passthrough runnables, they are stateless so shareable
    if not hasattr(setup_followup_query_transformation, "_passthrough_query"):
        setup_followup_query_transformation._passthrough_query = RunnablePassthrough()
    if not hasattr(setup_followup_query_transformation, "_passthrough_prev"):
        setup_followup_query_transformation._passthrough_prev = RunnablePassthrough()
    passthrough_query = setup_followup_query_transformation._passthrough_query
    passthrough_prev = setup_followup_query_transformation._passthrough_prev

    # StrOutputParser is stateless, can be reused
    if not hasattr(setup_followup_query_transformation, "_output_parser"):
        setup_followup_query_transformation._output_parser = StrOutputParser()
    output_parser = setup_followup_query_transformation._output_parser

    # Construct the chain, reusing stateless objects
    rewrite_chain = (
        {"query": passthrough_query, "previous_conversations": passthrough_prev}
        | query_rewrite_prompt
        | llm
        | output_parser
    )

    return rewrite_chain

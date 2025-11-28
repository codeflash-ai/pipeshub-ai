from typing import Optional

import httpx
from app.sources.client.http.http_request import HTTPRequest
from app.sources.client.http.http_response import HTTPResponse
from app.sources.client.iclient import IClient
from codeflash.verification.codeflash_capture import codeflash_capture


class HTTPClient(IClient):

    @codeflash_capture(function_name='HTTPClient.__init__', tmp_dir_path='/tmp/codeflash_1j5ekrv2/test_return_values', tests_root='/home/ubuntu/work/repo/backend/python/tests', is_fto=False)
    def __init__(self, token: str, token_type: str='Bearer', timeout: float=30.0, follow_redirects: bool=True) -> None:
        self.headers = {'Authorization': f'{token_type} {token}'}
        self.timeout = timeout
        self.follow_redirects = follow_redirects
        self.client: Optional[httpx.AsyncClient] = None

    def get_client(self) -> 'HTTPClient':
        """Get the client"""
        return self

    async def _ensure_client(self) -> httpx.AsyncClient:
        """Ensure client is created and available"""
        if self.client is None:
            self.client = httpx.AsyncClient(timeout=self.timeout, follow_redirects=self.follow_redirects)
        return self.client

    async def execute(self, request: HTTPRequest, **kwargs) -> HTTPResponse:
        """Execute an HTTP request
        Args:
            request: The HTTP request to execute
            kwargs: Additional keyword arguments to pass to the request
        Returns:
            A HTTPResponse object containing the response from the server
        """
        client = await self._ensure_client()
        if request.headers:
            merged_headers = dict(self.headers)
            merged_headers.update(request.headers)
        else:
            merged_headers = self.headers
        request_kwargs = {'params': request.query_params, 'headers': merged_headers, **kwargs}
        body = request.body
        if request.headers:
            content_type = request.headers.get('Content-Type', '').lower()
        else:
            content_type = ''
        if isinstance(body, dict):
            if 'application/x-www-form-urlencoded' in content_type:
                request_kwargs['data'] = body
            else:
                request_kwargs['json'] = body
        elif isinstance(body, bytes):
            request_kwargs['content'] = body
        response = await client.request(request.method, f'{request.url.format(**request.path_params)}', **request_kwargs)
        return HTTPResponse(response)

    async def close(self) -> None:
        """Close the client"""
        if self.client:
            await self.client.aclose()
            self.client = None

    async def __aenter__(self) -> 'HTTPClient':
        """Async context manager entry"""
        await self._ensure_client()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit"""
        await self.close()

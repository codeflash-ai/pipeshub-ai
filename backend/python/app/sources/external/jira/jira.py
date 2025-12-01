from typing import Any, Dict, Optional, Union

from app.sources.client.http.http_request import HTTPRequest
from app.sources.client.http.http_response import HTTPResponse
from app.sources.client.jira.jira import JiraClient
from codeflash.code_utils.codeflash_wrap_decorator import (
    codeflash_behavior_async, codeflash_performance_async)
from codeflash.verification.codeflash_capture import codeflash_capture


class JiraDataSource:

    @codeflash_capture(function_name='JiraDataSource.__init__', tmp_dir_path='/tmp/codeflash_1j5ekrv2/test_return_values', tests_root='/home/ubuntu/work/repo/backend/python/tests', is_fto=True)
    def __init__(self, client: JiraClient) -> None:
        """Default init for the connector-specific data source."""
        self._client = client.get_client()
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        try:
            self.base_url = self._client.get_base_url().rstrip('/')
        except AttributeError as exc:
            raise ValueError('HTTP client does not have get_base_url method') from exc

    def get_data_source(self) -> 'JiraDataSource':
        return self

    async def get_banner(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get announcement banner configuration

HTTP GET /rest/api/3/announcementBanner"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/announcementBanner'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_banner(self, isDismissible: Optional[bool]=None, isEnabled: Optional[bool]=None, message: Optional[str]=None, visibility: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update announcement banner configuration

HTTP PUT /rest/api/3/announcementBanner
Body (application/json) fields:
  - isDismissible (bool, optional)
  - isEnabled (bool, optional)
  - message (str, optional)
  - visibility (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if isDismissible is not None:
            _body['isDismissible'] = isDismissible
        if isEnabled is not None:
            _body['isEnabled'] = isEnabled
        if message is not None:
            _body['message'] = message
        if visibility is not None:
            _body['visibility'] = visibility
        rel_path = '/rest/api/3/announcementBanner'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_custom_fields_configurations(self, fieldIdsOrKeys: list[str], id: Optional[list[int]]=None, fieldContextId: Optional[list[int]]=None, issueId: Optional[int]=None, projectKeyOrId: Optional[str]=None, issueTypeId: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk get custom field configurations

HTTP POST /rest/api/3/app/field/context/configuration/list
Query params:
  - id (list[int], optional)
  - fieldContextId (list[int], optional)
  - issueId (int, optional)
  - projectKeyOrId (str, optional)
  - issueTypeId (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
Body (application/json) fields:
  - fieldIdsOrKeys (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if id is not None:
            _query['id'] = id
        if fieldContextId is not None:
            _query['fieldContextId'] = fieldContextId
        if issueId is not None:
            _query['issueId'] = issueId
        if projectKeyOrId is not None:
            _query['projectKeyOrId'] = projectKeyOrId
        if issueTypeId is not None:
            _query['issueTypeId'] = issueTypeId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body: Dict[str, Any] = {}
        _body['fieldIdsOrKeys'] = fieldIdsOrKeys
        rel_path = '/rest/api/3/app/field/context/configuration/list'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_multiple_custom_field_values(self, generateChangelog: Optional[bool]=None, updates: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update custom fields

HTTP POST /rest/api/3/app/field/value
Query params:
  - generateChangelog (bool, optional)
Body (application/json) fields:
  - updates (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if generateChangelog is not None:
            _query['generateChangelog'] = generateChangelog
        _body: Dict[str, Any] = {}
        if updates is not None:
            _body['updates'] = updates
        rel_path = '/rest/api/3/app/field/value'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_custom_field_configuration(self, fieldIdOrKey: str, id: Optional[list[int]]=None, fieldContextId: Optional[list[int]]=None, issueId: Optional[int]=None, projectKeyOrId: Optional[str]=None, issueTypeId: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get custom field configurations

HTTP GET /rest/api/3/app/field/{fieldIdOrKey}/context/configuration
Path params:
  - fieldIdOrKey (str)
Query params:
  - id (list[int], optional)
  - fieldContextId (list[int], optional)
  - issueId (int, optional)
  - projectKeyOrId (str, optional)
  - issueTypeId (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldIdOrKey': fieldIdOrKey}
        _query: Dict[str, Any] = {}
        if id is not None:
            _query['id'] = id
        if fieldContextId is not None:
            _query['fieldContextId'] = fieldContextId
        if issueId is not None:
            _query['issueId'] = issueId
        if projectKeyOrId is not None:
            _query['projectKeyOrId'] = projectKeyOrId
        if issueTypeId is not None:
            _query['issueTypeId'] = issueTypeId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/app/field/{fieldIdOrKey}/context/configuration'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_custom_field_configuration(self, fieldIdOrKey: str, configurations: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update custom field configurations

HTTP PUT /rest/api/3/app/field/{fieldIdOrKey}/context/configuration
Path params:
  - fieldIdOrKey (str)
Body (application/json) fields:
  - configurations (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldIdOrKey': fieldIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['configurations'] = configurations
        rel_path = '/rest/api/3/app/field/{fieldIdOrKey}/context/configuration'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_custom_field_value(self, fieldIdOrKey: str, generateChangelog: Optional[bool]=None, updates: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update custom field value

HTTP PUT /rest/api/3/app/field/{fieldIdOrKey}/value
Path params:
  - fieldIdOrKey (str)
Query params:
  - generateChangelog (bool, optional)
Body (application/json) fields:
  - updates (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldIdOrKey': fieldIdOrKey}
        _query: Dict[str, Any] = {}
        if generateChangelog is not None:
            _query['generateChangelog'] = generateChangelog
        _body: Dict[str, Any] = {}
        if updates is not None:
            _body['updates'] = updates
        rel_path = '/rest/api/3/app/field/{fieldIdOrKey}/value'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_application_property(self, key: Optional[str]=None, permissionLevel: Optional[str]=None, keyFilter: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get application property

HTTP GET /rest/api/3/application-properties
Query params:
  - key (str, optional)
  - permissionLevel (str, optional)
  - keyFilter (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if key is not None:
            _query['key'] = key
        if permissionLevel is not None:
            _query['permissionLevel'] = permissionLevel
        if keyFilter is not None:
            _query['keyFilter'] = keyFilter
        _body = None
        rel_path = '/rest/api/3/application-properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_advanced_settings(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get advanced settings

HTTP GET /rest/api/3/application-properties/advanced-settings"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/application-properties/advanced-settings'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_application_property(self, id: str, id_body: Optional[str]=None, value: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set application property

HTTP PUT /rest/api/3/application-properties/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - id (str, optional)
  - value (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if id_body is not None:
            _body['id'] = id_body
        if value is not None:
            _body['value'] = value
        rel_path = '/rest/api/3/application-properties/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_application_roles(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all application roles

HTTP GET /rest/api/3/applicationrole"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/applicationrole'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_application_role(self, key: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get application role

HTTP GET /rest/api/3/applicationrole/{key}
Path params:
  - key (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'key': key}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/applicationrole/{key}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_attachment_content(self, id: str, redirect: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get attachment content

HTTP GET /rest/api/3/attachment/content/{id}
Path params:
  - id (str)
Query params:
  - redirect (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if redirect is not None:
            _query['redirect'] = redirect
        _body = None
        rel_path = '/rest/api/3/attachment/content/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_attachment_meta(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get Jira attachment settings

HTTP GET /rest/api/3/attachment/meta"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/attachment/meta'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_attachment_thumbnail(self, id: str, redirect: Optional[bool]=None, fallbackToDefault: Optional[bool]=None, width: Optional[int]=None, height: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get attachment thumbnail

HTTP GET /rest/api/3/attachment/thumbnail/{id}
Path params:
  - id (str)
Query params:
  - redirect (bool, optional)
  - fallbackToDefault (bool, optional)
  - width (int, optional)
  - height (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if redirect is not None:
            _query['redirect'] = redirect
        if fallbackToDefault is not None:
            _query['fallbackToDefault'] = fallbackToDefault
        if width is not None:
            _query['width'] = width
        if height is not None:
            _query['height'] = height
        _body = None
        rel_path = '/rest/api/3/attachment/thumbnail/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_attachment(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete attachment

HTTP DELETE /rest/api/3/attachment/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/attachment/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_attachment(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get attachment metadata

HTTP GET /rest/api/3/attachment/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/attachment/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def expand_attachment_for_humans(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all metadata for an expanded attachment

HTTP GET /rest/api/3/attachment/{id}/expand/human
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/attachment/{id}/expand/human'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def expand_attachment_for_machines(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get contents metadata for an expanded attachment

HTTP GET /rest/api/3/attachment/{id}/expand/raw
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/attachment/{id}/expand/raw'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_audit_records(self, offset: Optional[int]=None, limit: Optional[int]=None, filter: Optional[str]=None, from_: Optional[str]=None, to: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get audit records

HTTP GET /rest/api/3/auditing/record
Query params:
  - offset (int, optional)
  - limit (int, optional)
  - filter (str, optional)
  - from (str, optional)
  - to (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if offset is not None:
            _query['offset'] = offset
        if limit is not None:
            _query['limit'] = limit
        if filter is not None:
            _query['filter'] = filter
        if from_ is not None:
            _query['from'] = from_
        if to is not None:
            _query['to'] = to
        _body = None
        rel_path = '/rest/api/3/auditing/record'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_system_avatars(self, type: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get system avatars by type

HTTP GET /rest/api/3/avatar/{type}/system
Path params:
  - type (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'type': type}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/avatar/{type}/system'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def submit_bulk_delete(self, selectedIssueIdsOrKeys: list[str], sendBulkNotification: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk delete issues

HTTP POST /rest/api/3/bulk/issues/delete
Body (application/json) fields:
  - selectedIssueIdsOrKeys (list[str], required)
  - sendBulkNotification (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['selectedIssueIdsOrKeys'] = selectedIssueIdsOrKeys
        if sendBulkNotification is not None:
            _body['sendBulkNotification'] = sendBulkNotification
        rel_path = '/rest/api/3/bulk/issues/delete'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_bulk_editable_fields(self, issueIdsOrKeys: str, searchText: Optional[str]=None, endingBefore: Optional[str]=None, startingAfter: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get bulk editable fields

HTTP GET /rest/api/3/bulk/issues/fields
Query params:
  - issueIdsOrKeys (str, required)
  - searchText (str, optional)
  - endingBefore (str, optional)
  - startingAfter (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['issueIdsOrKeys'] = issueIdsOrKeys
        if searchText is not None:
            _query['searchText'] = searchText
        if endingBefore is not None:
            _query['endingBefore'] = endingBefore
        if startingAfter is not None:
            _query['startingAfter'] = startingAfter
        _body = None
        rel_path = '/rest/api/3/bulk/issues/fields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def submit_bulk_edit(self, editedFieldsInput: Dict[str, Any], selectedActions: list[str], selectedIssueIdsOrKeys: list[str], sendBulkNotification: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk edit issues

HTTP POST /rest/api/3/bulk/issues/fields
Body (application/json) fields:
  - editedFieldsInput (Dict[str, Any], required)
  - selectedActions (list[str], required)
  - selectedIssueIdsOrKeys (list[str], required)
  - sendBulkNotification (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['editedFieldsInput'] = editedFieldsInput
        _body['selectedActions'] = selectedActions
        _body['selectedIssueIdsOrKeys'] = selectedIssueIdsOrKeys
        if sendBulkNotification is not None:
            _body['sendBulkNotification'] = sendBulkNotification
        rel_path = '/rest/api/3/bulk/issues/fields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def submit_bulk_move(self, sendBulkNotification: Optional[bool]=None, targetToSourcesMapping: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk move issues

HTTP POST /rest/api/3/bulk/issues/move
Body (application/json) fields:
  - sendBulkNotification (bool, optional)
  - targetToSourcesMapping (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if sendBulkNotification is not None:
            _body['sendBulkNotification'] = sendBulkNotification
        if targetToSourcesMapping is not None:
            _body['targetToSourcesMapping'] = targetToSourcesMapping
        rel_path = '/rest/api/3/bulk/issues/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_available_transitions(self, issueIdsOrKeys: str, endingBefore: Optional[str]=None, startingAfter: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get available transitions

HTTP GET /rest/api/3/bulk/issues/transition
Query params:
  - issueIdsOrKeys (str, required)
  - endingBefore (str, optional)
  - startingAfter (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['issueIdsOrKeys'] = issueIdsOrKeys
        if endingBefore is not None:
            _query['endingBefore'] = endingBefore
        if startingAfter is not None:
            _query['startingAfter'] = startingAfter
        _body = None
        rel_path = '/rest/api/3/bulk/issues/transition'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def submit_bulk_transition(self, bulkTransitionInputs: list[Dict[str, Any]], sendBulkNotification: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk transition issue statuses

HTTP POST /rest/api/3/bulk/issues/transition
Body (application/json) fields:
  - bulkTransitionInputs (list[Dict[str, Any]], required)
  - sendBulkNotification (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['bulkTransitionInputs'] = bulkTransitionInputs
        if sendBulkNotification is not None:
            _body['sendBulkNotification'] = sendBulkNotification
        rel_path = '/rest/api/3/bulk/issues/transition'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def submit_bulk_unwatch(self, selectedIssueIdsOrKeys: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk unwatch issues

HTTP POST /rest/api/3/bulk/issues/unwatch
Body (application/json) fields:
  - selectedIssueIdsOrKeys (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['selectedIssueIdsOrKeys'] = selectedIssueIdsOrKeys
        rel_path = '/rest/api/3/bulk/issues/unwatch'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def submit_bulk_watch(self, selectedIssueIdsOrKeys: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk watch issues

HTTP POST /rest/api/3/bulk/issues/watch
Body (application/json) fields:
  - selectedIssueIdsOrKeys (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['selectedIssueIdsOrKeys'] = selectedIssueIdsOrKeys
        rel_path = '/rest/api/3/bulk/issues/watch'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_bulk_operation_progress(self, taskId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get bulk issue operation progress

HTTP GET /rest/api/3/bulk/queue/{taskId}
Path params:
  - taskId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'taskId': taskId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/bulk/queue/{taskId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_bulk_changelogs(self, issueIdsOrKeys: list[str], fieldIds: Optional[list[str]]=None, maxResults: Optional[int]=None, nextPageToken: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk fetch changelogs

HTTP POST /rest/api/3/changelog/bulkfetch
Body (application/json) fields:
  - fieldIds (list[str], optional)
  - issueIdsOrKeys (list[str], required)
  - maxResults (int, optional)
  - nextPageToken (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if fieldIds is not None:
            _body['fieldIds'] = fieldIds
        _body['issueIdsOrKeys'] = issueIdsOrKeys
        if maxResults is not None:
            _body['maxResults'] = maxResults
        if nextPageToken is not None:
            _body['nextPageToken'] = nextPageToken
        rel_path = '/rest/api/3/changelog/bulkfetch'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_user_data_classification_levels(self, status: Optional[list[str]]=None, orderBy: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all classification levels

HTTP GET /rest/api/3/classification-levels
Query params:
  - status (list[str], optional)
  - orderBy (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if status is not None:
            _query['status'] = status
        if orderBy is not None:
            _query['orderBy'] = orderBy
        _body = None
        rel_path = '/rest/api/3/classification-levels'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_comments_by_ids(self, ids: list[int], expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get comments by IDs

HTTP POST /rest/api/3/comment/list
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - ids (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        _body['ids'] = ids
        rel_path = '/rest/api/3/comment/list'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_comment_property_keys(self, commentId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get comment property keys

HTTP GET /rest/api/3/comment/{commentId}/properties
Path params:
  - commentId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'commentId': commentId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/comment/{commentId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_comment_property(self, commentId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete comment property

HTTP DELETE /rest/api/3/comment/{commentId}/properties/{propertyKey}
Path params:
  - commentId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'commentId': commentId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/comment/{commentId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_comment_property(self, commentId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get comment property

HTTP GET /rest/api/3/comment/{commentId}/properties/{propertyKey}
Path params:
  - commentId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'commentId': commentId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/comment/{commentId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_comment_property(self, commentId: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set comment property

HTTP PUT /rest/api/3/comment/{commentId}/properties/{propertyKey}
Path params:
  - commentId (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'commentId': commentId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/comment/{commentId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_components_for_projects(self, projectIdsOrKeys: Optional[list[str]]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, orderBy: Optional[str]=None, query: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find components for projects

HTTP GET /rest/api/3/component
Query params:
  - projectIdsOrKeys (list[str], optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - orderBy (str, optional)
  - query (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if projectIdsOrKeys is not None:
            _query['projectIdsOrKeys'] = projectIdsOrKeys
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if query is not None:
            _query['query'] = query
        _body = None
        rel_path = '/rest/api/3/component'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_component(self, ari: Optional[str]=None, assignee: Optional[Dict[str, Any]]=None, assigneeType: Optional[str]=None, description: Optional[str]=None, id: Optional[str]=None, isAssigneeTypeValid: Optional[bool]=None, lead: Optional[Dict[str, Any]]=None, leadAccountId: Optional[str]=None, leadUserName: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, name: Optional[str]=None, project: Optional[str]=None, projectId: Optional[int]=None, realAssignee: Optional[Dict[str, Any]]=None, realAssigneeType: Optional[str]=None, self_: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create component

HTTP POST /rest/api/3/component
Body (application/json) fields:
  - ari (str, optional)
  - assignee (Dict[str, Any], optional)
  - assigneeType (str, optional)
  - description (str, optional)
  - id (str, optional)
  - isAssigneeTypeValid (bool, optional)
  - lead (Dict[str, Any], optional)
  - leadAccountId (str, optional)
  - leadUserName (str, optional)
  - metadata (Dict[str, Any], optional)
  - name (str, optional)
  - project (str, optional)
  - projectId (int, optional)
  - realAssignee (Dict[str, Any], optional)
  - realAssigneeType (str, optional)
  - self (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if ari is not None:
            _body['ari'] = ari
        if assignee is not None:
            _body['assignee'] = assignee
        if assigneeType is not None:
            _body['assigneeType'] = assigneeType
        if description is not None:
            _body['description'] = description
        if id is not None:
            _body['id'] = id
        if isAssigneeTypeValid is not None:
            _body['isAssigneeTypeValid'] = isAssigneeTypeValid
        if lead is not None:
            _body['lead'] = lead
        if leadAccountId is not None:
            _body['leadAccountId'] = leadAccountId
        if leadUserName is not None:
            _body['leadUserName'] = leadUserName
        if metadata is not None:
            _body['metadata'] = metadata
        if name is not None:
            _body['name'] = name
        if project is not None:
            _body['project'] = project
        if projectId is not None:
            _body['projectId'] = projectId
        if realAssignee is not None:
            _body['realAssignee'] = realAssignee
        if realAssigneeType is not None:
            _body['realAssigneeType'] = realAssigneeType
        if self_ is not None:
            _body['self'] = self_
        rel_path = '/rest/api/3/component'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_component(self, id: str, moveIssuesTo: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete component

HTTP DELETE /rest/api/3/component/{id}
Path params:
  - id (str)
Query params:
  - moveIssuesTo (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if moveIssuesTo is not None:
            _query['moveIssuesTo'] = moveIssuesTo
        _body = None
        rel_path = '/rest/api/3/component/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_component(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get component

HTTP GET /rest/api/3/component/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/component/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_component(self, id: str, ari: Optional[str]=None, assignee: Optional[Dict[str, Any]]=None, assigneeType: Optional[str]=None, description: Optional[str]=None, id_body: Optional[str]=None, isAssigneeTypeValid: Optional[bool]=None, lead: Optional[Dict[str, Any]]=None, leadAccountId: Optional[str]=None, leadUserName: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None, name: Optional[str]=None, project: Optional[str]=None, projectId: Optional[int]=None, realAssignee: Optional[Dict[str, Any]]=None, realAssigneeType: Optional[str]=None, self_: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update component

HTTP PUT /rest/api/3/component/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - ari (str, optional)
  - assignee (Dict[str, Any], optional)
  - assigneeType (str, optional)
  - description (str, optional)
  - id (str, optional)
  - isAssigneeTypeValid (bool, optional)
  - lead (Dict[str, Any], optional)
  - leadAccountId (str, optional)
  - leadUserName (str, optional)
  - metadata (Dict[str, Any], optional)
  - name (str, optional)
  - project (str, optional)
  - projectId (int, optional)
  - realAssignee (Dict[str, Any], optional)
  - realAssigneeType (str, optional)
  - self (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if ari is not None:
            _body['ari'] = ari
        if assignee is not None:
            _body['assignee'] = assignee
        if assigneeType is not None:
            _body['assigneeType'] = assigneeType
        if description is not None:
            _body['description'] = description
        if id_body is not None:
            _body['id'] = id_body
        if isAssigneeTypeValid is not None:
            _body['isAssigneeTypeValid'] = isAssigneeTypeValid
        if lead is not None:
            _body['lead'] = lead
        if leadAccountId is not None:
            _body['leadAccountId'] = leadAccountId
        if leadUserName is not None:
            _body['leadUserName'] = leadUserName
        if metadata is not None:
            _body['metadata'] = metadata
        if name is not None:
            _body['name'] = name
        if project is not None:
            _body['project'] = project
        if projectId is not None:
            _body['projectId'] = projectId
        if realAssignee is not None:
            _body['realAssignee'] = realAssignee
        if realAssigneeType is not None:
            _body['realAssigneeType'] = realAssigneeType
        if self_ is not None:
            _body['self'] = self_
        rel_path = '/rest/api/3/component/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_component_related_issues(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get component issues count

HTTP GET /rest/api/3/component/{id}/relatedIssueCounts
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/component/{id}/relatedIssueCounts'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_configuration(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get global settings

HTTP GET /rest/api/3/configuration"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/configuration'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_selected_time_tracking_implementation(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get selected time tracking provider

HTTP GET /rest/api/3/configuration/timetracking"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/configuration/timetracking'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def select_time_tracking_implementation(self, key: str, name: Optional[str]=None, url: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Select time tracking provider

HTTP PUT /rest/api/3/configuration/timetracking
Body (application/json) fields:
  - key (str, required)
  - name (str, optional)
  - url (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['key'] = key
        if name is not None:
            _body['name'] = name
        if url is not None:
            _body['url'] = url
        rel_path = '/rest/api/3/configuration/timetracking'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_available_time_tracking_implementations(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all time tracking providers

HTTP GET /rest/api/3/configuration/timetracking/list"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/configuration/timetracking/list'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_shared_time_tracking_configuration(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get time tracking settings

HTTP GET /rest/api/3/configuration/timetracking/options"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/configuration/timetracking/options'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_shared_time_tracking_configuration(self, defaultUnit: str, timeFormat: str, workingDaysPerWeek: float, workingHoursPerDay: float, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set time tracking settings

HTTP PUT /rest/api/3/configuration/timetracking/options
Body (application/json) fields:
  - defaultUnit (str, required)
  - timeFormat (str, required)
  - workingDaysPerWeek (float, required)
  - workingHoursPerDay (float, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['defaultUnit'] = defaultUnit
        _body['timeFormat'] = timeFormat
        _body['workingDaysPerWeek'] = workingDaysPerWeek
        _body['workingHoursPerDay'] = workingHoursPerDay
        rel_path = '/rest/api/3/configuration/timetracking/options'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_custom_field_option(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get custom field option

HTTP GET /rest/api/3/customFieldOption/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/customFieldOption/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_dashboards(self, filter: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all dashboards

HTTP GET /rest/api/3/dashboard
Query params:
  - filter (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if filter is not None:
            _query['filter'] = filter
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/dashboard'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_dashboard(self, editPermissions: list[Dict[str, Any]], name: str, sharePermissions: list[Dict[str, Any]], extendAdminPermissions: Optional[bool]=None, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create dashboard

HTTP POST /rest/api/3/dashboard
Query params:
  - extendAdminPermissions (bool, optional)
Body (application/json) fields:
  - description (str, optional)
  - editPermissions (list[Dict[str, Any]], required)
  - name (str, required)
  - sharePermissions (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if extendAdminPermissions is not None:
            _query['extendAdminPermissions'] = extendAdminPermissions
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['editPermissions'] = editPermissions
        _body['name'] = name
        _body['sharePermissions'] = sharePermissions
        rel_path = '/rest/api/3/dashboard'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_edit_dashboards(self, action: str, entityIds: list[int], changeOwnerDetails: Optional[Dict[str, Any]]=None, extendAdminPermissions: Optional[bool]=None, permissionDetails: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk edit dashboards

HTTP PUT /rest/api/3/dashboard/bulk/edit
Body (application/json) fields:
  - action (str, required)
  - changeOwnerDetails (Dict[str, Any], optional)
  - entityIds (list[int], required)
  - extendAdminPermissions (bool, optional)
  - permissionDetails (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['action'] = action
        if changeOwnerDetails is not None:
            _body['changeOwnerDetails'] = changeOwnerDetails
        _body['entityIds'] = entityIds
        if extendAdminPermissions is not None:
            _body['extendAdminPermissions'] = extendAdminPermissions
        if permissionDetails is not None:
            _body['permissionDetails'] = permissionDetails
        rel_path = '/rest/api/3/dashboard/bulk/edit'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_available_dashboard_gadgets(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get available gadgets

HTTP GET /rest/api/3/dashboard/gadgets"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/gadgets'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_dashboards_paginated(self, dashboardName: Optional[str]=None, accountId: Optional[str]=None, owner: Optional[str]=None, groupname: Optional[str]=None, groupId: Optional[str]=None, projectId: Optional[int]=None, orderBy: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, status: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search for dashboards

HTTP GET /rest/api/3/dashboard/search
Query params:
  - dashboardName (str, optional)
  - accountId (str, optional)
  - owner (str, optional)
  - groupname (str, optional)
  - groupId (str, optional)
  - projectId (int, optional)
  - orderBy (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - status (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if dashboardName is not None:
            _query['dashboardName'] = dashboardName
        if accountId is not None:
            _query['accountId'] = accountId
        if owner is not None:
            _query['owner'] = owner
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        if projectId is not None:
            _query['projectId'] = projectId
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if status is not None:
            _query['status'] = status
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/dashboard/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_gadgets(self, dashboardId: int, moduleKey: Optional[list[str]]=None, uri: Optional[list[str]]=None, gadgetId: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get gadgets

HTTP GET /rest/api/3/dashboard/{dashboardId}/gadget
Path params:
  - dashboardId (int)
Query params:
  - moduleKey (list[str], optional)
  - uri (list[str], optional)
  - gadgetId (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'dashboardId': dashboardId}
        _query: Dict[str, Any] = {}
        if moduleKey is not None:
            _query['moduleKey'] = moduleKey
        if uri is not None:
            _query['uri'] = uri
        if gadgetId is not None:
            _query['gadgetId'] = gadgetId
        _body = None
        rel_path = '/rest/api/3/dashboard/{dashboardId}/gadget'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_gadget(self, dashboardId: int, color: Optional[str]=None, ignoreUriAndModuleKeyValidation: Optional[bool]=None, moduleKey: Optional[str]=None, position: Optional[Dict[str, Any]]=None, title: Optional[str]=None, uri: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add gadget to dashboard

HTTP POST /rest/api/3/dashboard/{dashboardId}/gadget
Path params:
  - dashboardId (int)
Body (application/json) fields:
  - color (str, optional)
  - ignoreUriAndModuleKeyValidation (bool, optional)
  - moduleKey (str, optional)
  - position (Dict[str, Any], optional)
  - title (str, optional)
  - uri (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'dashboardId': dashboardId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if color is not None:
            _body['color'] = color
        if ignoreUriAndModuleKeyValidation is not None:
            _body['ignoreUriAndModuleKeyValidation'] = ignoreUriAndModuleKeyValidation
        if moduleKey is not None:
            _body['moduleKey'] = moduleKey
        if position is not None:
            _body['position'] = position
        if title is not None:
            _body['title'] = title
        if uri is not None:
            _body['uri'] = uri
        rel_path = '/rest/api/3/dashboard/{dashboardId}/gadget'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_gadget(self, dashboardId: int, gadgetId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove gadget from dashboard

HTTP DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}
Path params:
  - dashboardId (int)
  - gadgetId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'dashboardId': dashboardId, 'gadgetId': gadgetId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_gadget(self, dashboardId: int, gadgetId: int, color: Optional[str]=None, position: Optional[Dict[str, Any]]=None, title: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update gadget on dashboard

HTTP PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}
Path params:
  - dashboardId (int)
  - gadgetId (int)
Body (application/json) fields:
  - color (str, optional)
  - position (Dict[str, Any], optional)
  - title (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'dashboardId': dashboardId, 'gadgetId': gadgetId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if color is not None:
            _body['color'] = color
        if position is not None:
            _body['position'] = position
        if title is not None:
            _body['title'] = title
        rel_path = '/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_dashboard_item_property_keys(self, dashboardId: str, itemId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get dashboard item property keys

HTTP GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties
Path params:
  - dashboardId (str)
  - itemId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'dashboardId': dashboardId, 'itemId': itemId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_dashboard_item_property(self, dashboardId: str, itemId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete dashboard item property

HTTP DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
Path params:
  - dashboardId (str)
  - itemId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'dashboardId': dashboardId, 'itemId': itemId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_dashboard_item_property(self, dashboardId: str, itemId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get dashboard item property

HTTP GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
Path params:
  - dashboardId (str)
  - itemId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'dashboardId': dashboardId, 'itemId': itemId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_dashboard_item_property(self, dashboardId: str, itemId: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set dashboard item property

HTTP PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}
Path params:
  - dashboardId (str)
  - itemId (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'dashboardId': dashboardId, 'itemId': itemId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_dashboard(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete dashboard

HTTP DELETE /rest/api/3/dashboard/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_dashboard(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get dashboard

HTTP GET /rest/api/3/dashboard/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/dashboard/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_dashboard(self, id: str, editPermissions: list[Dict[str, Any]], name: str, sharePermissions: list[Dict[str, Any]], extendAdminPermissions: Optional[bool]=None, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update dashboard

HTTP PUT /rest/api/3/dashboard/{id}
Path params:
  - id (str)
Query params:
  - extendAdminPermissions (bool, optional)
Body (application/json) fields:
  - description (str, optional)
  - editPermissions (list[Dict[str, Any]], required)
  - name (str, required)
  - sharePermissions (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if extendAdminPermissions is not None:
            _query['extendAdminPermissions'] = extendAdminPermissions
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['editPermissions'] = editPermissions
        _body['name'] = name
        _body['sharePermissions'] = sharePermissions
        rel_path = '/rest/api/3/dashboard/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def copy_dashboard(self, id: str, editPermissions: list[Dict[str, Any]], name: str, sharePermissions: list[Dict[str, Any]], extendAdminPermissions: Optional[bool]=None, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Copy dashboard

HTTP POST /rest/api/3/dashboard/{id}/copy
Path params:
  - id (str)
Query params:
  - extendAdminPermissions (bool, optional)
Body (application/json) fields:
  - description (str, optional)
  - editPermissions (list[Dict[str, Any]], required)
  - name (str, required)
  - sharePermissions (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if extendAdminPermissions is not None:
            _query['extendAdminPermissions'] = extendAdminPermissions
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['editPermissions'] = editPermissions
        _body['name'] = name
        _body['sharePermissions'] = sharePermissions
        rel_path = '/rest/api/3/dashboard/{id}/copy'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_policy(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get data policy for the workspace

HTTP GET /rest/api/3/data-policy"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/data-policy'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_policies(self, ids: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get data policy for projects

HTTP GET /rest/api/3/data-policy/project
Query params:
  - ids (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if ids is not None:
            _query['ids'] = ids
        _body = None
        rel_path = '/rest/api/3/data-policy/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_events(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get events

HTTP GET /rest/api/3/events"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/events'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def analyse_expression(self, expressions: list[str], check: Optional[str]=None, contextVariables: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Analyse Jira expression

HTTP POST /rest/api/3/expression/analyse
Query params:
  - check (str, optional)
Body (application/json) fields:
  - contextVariables (Dict[str, Any], optional)
  - expressions (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if check is not None:
            _query['check'] = check
        _body: Dict[str, Any] = {}
        if contextVariables is not None:
            _body['contextVariables'] = contextVariables
        _body['expressions'] = expressions
        rel_path = '/rest/api/3/expression/analyse'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def evaluate_jira_expression(self, expression: str, expand: Optional[str]=None, context: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Currently being removed. Evaluate Jira expression

HTTP POST /rest/api/3/expression/eval
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - context (Dict[str, Any], optional)
  - expression (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if context is not None:
            _body['context'] = context
        _body['expression'] = expression
        rel_path = '/rest/api/3/expression/eval'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def evaluate_jsis_jira_expression(self, expression: str, expand: Optional[str]=None, context: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Evaluate Jira expression using enhanced search API

HTTP POST /rest/api/3/expression/evaluate
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - context (Dict[str, Any], optional)
  - expression (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if context is not None:
            _body['context'] = context
        _body['expression'] = expression
        rel_path = '/rest/api/3/expression/evaluate'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_fields(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get fields

HTTP GET /rest/api/3/field"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_custom_field(self, name: str, type: str, description: Optional[str]=None, searcherKey: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create custom field

HTTP POST /rest/api/3/field
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)
  - searcherKey (str, optional)
  - type (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        if searcherKey is not None:
            _body['searcherKey'] = searcherKey
        _body['type'] = type
        rel_path = '/rest/api/3/field'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_associations(self, associationContexts: list[Dict[str, Any]], fields: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove associations

HTTP DELETE /rest/api/3/field/association
Body (application/json) fields:
  - associationContexts (list[Dict[str, Any]], required)
  - fields (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['associationContexts'] = associationContexts
        _body['fields'] = fields
        rel_path = '/rest/api/3/field/association'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_associations(self, associationContexts: list[Dict[str, Any]], fields: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create associations

HTTP PUT /rest/api/3/field/association
Body (application/json) fields:
  - associationContexts (list[Dict[str, Any]], required)
  - fields (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['associationContexts'] = associationContexts
        _body['fields'] = fields
        rel_path = '/rest/api/3/field/association'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_fields_paginated(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, type: Optional[list[str]]=None, id: Optional[list[str]]=None, query: Optional[str]=None, orderBy: Optional[str]=None, expand: Optional[str]=None, projectIds: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get fields paginated

HTTP GET /rest/api/3/field/search
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - type (list[str], optional)
  - id (list[str], optional)
  - query (str, optional)
  - orderBy (str, optional)
  - expand (str, optional)
  - projectIds (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if type is not None:
            _query['type'] = type
        if id is not None:
            _query['id'] = id
        if query is not None:
            _query['query'] = query
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if expand is not None:
            _query['expand'] = expand
        if projectIds is not None:
            _query['projectIds'] = projectIds
        _body = None
        rel_path = '/rest/api/3/field/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_trashed_fields_paginated(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[str]]=None, query: Optional[str]=None, expand: Optional[str]=None, orderBy: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get fields in trash paginated

HTTP GET /rest/api/3/field/search/trashed
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[str], optional)
  - query (str, optional)
  - expand (str, optional)
  - orderBy (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if query is not None:
            _query['query'] = query
        if expand is not None:
            _query['expand'] = expand
        if orderBy is not None:
            _query['orderBy'] = orderBy
        _body = None
        rel_path = '/rest/api/3/field/search/trashed'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_custom_field(self, fieldId: str, description: Optional[str]=None, name: Optional[str]=None, searcherKey: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update custom field

HTTP PUT /rest/api/3/field/{fieldId}
Path params:
  - fieldId (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)
  - searcherKey (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        if searcherKey is not None:
            _body['searcherKey'] = searcherKey
        rel_path = '/rest/api/3/field/{fieldId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_contexts_for_field(self, fieldId: str, isAnyIssueType: Optional[bool]=None, isGlobalContext: Optional[bool]=None, contextId: Optional[list[int]]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get custom field contexts

HTTP GET /rest/api/3/field/{fieldId}/context
Path params:
  - fieldId (str)
Query params:
  - isAnyIssueType (bool, optional)
  - isGlobalContext (bool, optional)
  - contextId (list[int], optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if isAnyIssueType is not None:
            _query['isAnyIssueType'] = isAnyIssueType
        if isGlobalContext is not None:
            _query['isGlobalContext'] = isGlobalContext
        if contextId is not None:
            _query['contextId'] = contextId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_custom_field_context(self, fieldId: str, name: str, description: Optional[str]=None, id: Optional[str]=None, issueTypeIds: Optional[list[str]]=None, projectIds: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create custom field context

HTTP POST /rest/api/3/field/{fieldId}/context
Path params:
  - fieldId (str)
Body (application/json) fields:
  - description (str, optional)
  - id (str, optional)
  - issueTypeIds (list[str], optional)
  - name (str, required)
  - projectIds (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if id is not None:
            _body['id'] = id
        if issueTypeIds is not None:
            _body['issueTypeIds'] = issueTypeIds
        _body['name'] = name
        if projectIds is not None:
            _body['projectIds'] = projectIds
        rel_path = '/rest/api/3/field/{fieldId}/context'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_default_values(self, fieldId: str, contextId: Optional[list[int]]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get custom field contexts default values

HTTP GET /rest/api/3/field/{fieldId}/context/defaultValue
Path params:
  - fieldId (str)
Query params:
  - contextId (list[int], optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if contextId is not None:
            _query['contextId'] = contextId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/defaultValue'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_default_values(self, fieldId: str, defaultValues: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set custom field contexts default values

HTTP PUT /rest/api/3/field/{fieldId}/context/defaultValue
Path params:
  - fieldId (str)
Body (application/json) fields:
  - defaultValues (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultValues is not None:
            _body['defaultValues'] = defaultValues
        rel_path = '/rest/api/3/field/{fieldId}/context/defaultValue'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_mappings_for_contexts(self, fieldId: str, contextId: Optional[list[int]]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue types for custom field context

HTTP GET /rest/api/3/field/{fieldId}/context/issuetypemapping
Path params:
  - fieldId (str)
Query params:
  - contextId (list[int], optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if contextId is not None:
            _query['contextId'] = contextId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/issuetypemapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_custom_field_contexts_for_projects_and_issue_types(self, fieldId: str, mappings: list[Dict[str, Any]], startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get custom field contexts for projects and issue types

HTTP POST /rest/api/3/field/{fieldId}/context/mapping
Path params:
  - fieldId (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
Body (application/json) fields:
  - mappings (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body: Dict[str, Any] = {}
        _body['mappings'] = mappings
        rel_path = '/rest/api/3/field/{fieldId}/context/mapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_context_mapping(self, fieldId: str, contextId: Optional[list[int]]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project mappings for custom field context

HTTP GET /rest/api/3/field/{fieldId}/context/projectmapping
Path params:
  - fieldId (str)
Query params:
  - contextId (list[int], optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if contextId is not None:
            _query['contextId'] = contextId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/projectmapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_custom_field_context(self, fieldId: str, contextId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete custom field context

HTTP DELETE /rest/api/3/field/{fieldId}/context/{contextId}
Path params:
  - fieldId (str)
  - contextId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_custom_field_context(self, fieldId: str, contextId: int, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update custom field context

HTTP PUT /rest/api/3/field/{fieldId}/context/{contextId}
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_issue_types_to_context(self, fieldId: str, contextId: int, issueTypeIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add issue types to context

HTTP PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - issueTypeIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeIds'] = issueTypeIds
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/issuetype'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_issue_types_from_context(self, fieldId: str, contextId: int, issueTypeIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove issue types from context

HTTP POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - issueTypeIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeIds'] = issueTypeIds
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_options_for_context(self, fieldId: str, contextId: int, optionId: Optional[int]=None, onlyOptions: Optional[bool]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get custom field options (context)

HTTP GET /rest/api/3/field/{fieldId}/context/{contextId}/option
Path params:
  - fieldId (str)
  - contextId (int)
Query params:
  - optionId (int, optional)
  - onlyOptions (bool, optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        if optionId is not None:
            _query['optionId'] = optionId
        if onlyOptions is not None:
            _query['onlyOptions'] = onlyOptions
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/option'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_custom_field_option(self, fieldId: str, contextId: int, options: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create custom field options (context)

HTTP POST /rest/api/3/field/{fieldId}/context/{contextId}/option
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - options (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if options is not None:
            _body['options'] = options
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/option'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_custom_field_option(self, fieldId: str, contextId: int, options: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update custom field options (context)

HTTP PUT /rest/api/3/field/{fieldId}/context/{contextId}/option
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - options (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if options is not None:
            _body['options'] = options
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/option'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def reorder_custom_field_options(self, fieldId: str, contextId: int, customFieldOptionIds: list[str], after: Optional[str]=None, position: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Reorder custom field options (context)

HTTP PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - after (str, optional)
  - customFieldOptionIds (list[str], required)
  - position (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if after is not None:
            _body['after'] = after
        _body['customFieldOptionIds'] = customFieldOptionIds
        if position is not None:
            _body['position'] = position
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/option/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_custom_field_option(self, fieldId: str, contextId: int, optionId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete custom field options (context)

HTTP DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}
Path params:
  - fieldId (str)
  - contextId (int)
  - optionId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId, 'optionId': optionId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def replace_custom_field_option(self, fieldId: str, optionId: int, contextId: int, replaceWith: Optional[int]=None, jql: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Replace custom field options

HTTP DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue
Path params:
  - fieldId (str)
  - optionId (int)
  - contextId (int)
Query params:
  - replaceWith (int, optional)
  - jql (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId, 'optionId': optionId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        if replaceWith is not None:
            _query['replaceWith'] = replaceWith
        if jql is not None:
            _query['jql'] = jql
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_projects_to_custom_field_context(self, fieldId: str, contextId: int, projectIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign custom field context to projects

HTTP PUT /rest/api/3/field/{fieldId}/context/{contextId}/project
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - projectIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['projectIds'] = projectIds
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_custom_field_context_from_projects(self, fieldId: str, contextId: int, projectIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove custom field context from projects

HTTP POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove
Path params:
  - fieldId (str)
  - contextId (int)
Body (application/json) fields:
  - projectIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldId': fieldId, 'contextId': contextId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['projectIds'] = projectIds
        rel_path = '/rest/api/3/field/{fieldId}/context/{contextId}/project/remove'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_contexts_for_field_deprecated(self, fieldId: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get contexts for a field

HTTP GET /rest/api/3/field/{fieldId}/contexts
Path params:
  - fieldId (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/contexts'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_screens_for_field(self, fieldId: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get screens for a field

HTTP GET /rest/api/3/field/{fieldId}/screens
Path params:
  - fieldId (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/field/{fieldId}/screens'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_issue_field_options(self, fieldKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all issue field options

HTTP GET /rest/api/3/field/{fieldKey}/option
Path params:
  - fieldKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldKey': fieldKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/field/{fieldKey}/option'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_field_option(self, fieldKey: str, value: str, config: Optional[Dict[str, Any]]=None, properties: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue field option

HTTP POST /rest/api/3/field/{fieldKey}/option
Path params:
  - fieldKey (str)
Body (application/json) fields:
  - config (Dict[str, Any], optional)
  - properties (Dict[str, Any], optional)
  - value (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldKey': fieldKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if config is not None:
            _body['config'] = config
        if properties is not None:
            _body['properties'] = properties
        _body['value'] = value
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/field/{fieldKey}/option'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_selectable_issue_field_options(self, fieldKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, projectId: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get selectable issue field options

HTTP GET /rest/api/3/field/{fieldKey}/option/suggestions/edit
Path params:
  - fieldKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - projectId (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldKey': fieldKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if projectId is not None:
            _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/field/{fieldKey}/option/suggestions/edit'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_visible_issue_field_options(self, fieldKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, projectId: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get visible issue field options

HTTP GET /rest/api/3/field/{fieldKey}/option/suggestions/search
Path params:
  - fieldKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - projectId (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldKey': fieldKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if projectId is not None:
            _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/field/{fieldKey}/option/suggestions/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue_field_option(self, fieldKey: str, optionId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue field option

HTTP DELETE /rest/api/3/field/{fieldKey}/option/{optionId}
Path params:
  - fieldKey (str)
  - optionId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldKey': fieldKey, 'optionId': optionId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{fieldKey}/option/{optionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_field_option(self, fieldKey: str, optionId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue field option

HTTP GET /rest/api/3/field/{fieldKey}/option/{optionId}
Path params:
  - fieldKey (str)
  - optionId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldKey': fieldKey, 'optionId': optionId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{fieldKey}/option/{optionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_issue_field_option(self, fieldKey: str, optionId: int, id: int, value: str, config: Optional[Dict[str, Any]]=None, properties: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue field option

HTTP PUT /rest/api/3/field/{fieldKey}/option/{optionId}
Path params:
  - fieldKey (str)
  - optionId (int)
Body (application/json) fields:
  - config (Dict[str, Any], optional)
  - id (int, required)
  - properties (Dict[str, Any], optional)
  - value (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'fieldKey': fieldKey, 'optionId': optionId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if config is not None:
            _body['config'] = config
        _body['id'] = id
        if properties is not None:
            _body['properties'] = properties
        _body['value'] = value
        rel_path = '/rest/api/3/field/{fieldKey}/option/{optionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def replace_issue_field_option(self, fieldKey: str, optionId: int, replaceWith: Optional[int]=None, jql: Optional[str]=None, overrideScreenSecurity: Optional[bool]=None, overrideEditableFlag: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Replace issue field option

HTTP DELETE /rest/api/3/field/{fieldKey}/option/{optionId}/issue
Path params:
  - fieldKey (str)
  - optionId (int)
Query params:
  - replaceWith (int, optional)
  - jql (str, optional)
  - overrideScreenSecurity (bool, optional)
  - overrideEditableFlag (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldKey': fieldKey, 'optionId': optionId}
        _query: Dict[str, Any] = {}
        if replaceWith is not None:
            _query['replaceWith'] = replaceWith
        if jql is not None:
            _query['jql'] = jql
        if overrideScreenSecurity is not None:
            _query['overrideScreenSecurity'] = overrideScreenSecurity
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body = None
        rel_path = '/rest/api/3/field/{fieldKey}/option/{optionId}/issue'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_custom_field(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete custom field

HTTP DELETE /rest/api/3/field/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def restore_custom_field(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Restore custom field from trash

HTTP POST /rest/api/3/field/{id}/restore
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{id}/restore'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def trash_custom_field(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Move custom field to trash

HTTP POST /rest/api/3/field/{id}/trash
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/field/{id}/trash'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_field_configurations(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[int]]=None, isDefault: Optional[bool]=None, query: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all field configurations

HTTP GET /rest/api/3/fieldconfiguration
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[int], optional)
  - isDefault (bool, optional)
  - query (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if isDefault is not None:
            _query['isDefault'] = isDefault
        if query is not None:
            _query['query'] = query
        _body = None
        rel_path = '/rest/api/3/fieldconfiguration'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_field_configuration(self, name: str, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create field configuration

HTTP POST /rest/api/3/fieldconfiguration
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        rel_path = '/rest/api/3/fieldconfiguration'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_field_configuration(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete field configuration

HTTP DELETE /rest/api/3/fieldconfiguration/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/fieldconfiguration/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_field_configuration(self, id: int, name: str, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update field configuration

HTTP PUT /rest/api/3/fieldconfiguration/{id}
Path params:
  - id (int)
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        rel_path = '/rest/api/3/fieldconfiguration/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_field_configuration_items(self, id: int, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get field configuration items

HTTP GET /rest/api/3/fieldconfiguration/{id}/fields
Path params:
  - id (int)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/fieldconfiguration/{id}/fields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_field_configuration_items(self, id: int, fieldConfigurationItems: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update field configuration items

HTTP PUT /rest/api/3/fieldconfiguration/{id}/fields
Path params:
  - id (int)
Body (application/json) fields:
  - fieldConfigurationItems (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['fieldConfigurationItems'] = fieldConfigurationItems
        rel_path = '/rest/api/3/fieldconfiguration/{id}/fields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_field_configuration_schemes(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all field configuration schemes

HTTP GET /rest/api/3/fieldconfigurationscheme
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        _body = None
        rel_path = '/rest/api/3/fieldconfigurationscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_field_configuration_scheme(self, name: str, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create field configuration scheme

HTTP POST /rest/api/3/fieldconfigurationscheme
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        rel_path = '/rest/api/3/fieldconfigurationscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_field_configuration_scheme_mappings(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, fieldConfigurationSchemeId: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get field configuration issue type items

HTTP GET /rest/api/3/fieldconfigurationscheme/mapping
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - fieldConfigurationSchemeId (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if fieldConfigurationSchemeId is not None:
            _query['fieldConfigurationSchemeId'] = fieldConfigurationSchemeId
        _body = None
        rel_path = '/rest/api/3/fieldconfigurationscheme/mapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_field_configuration_scheme_project_mapping(self, projectId: list[int], startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get field configuration schemes for projects

HTTP GET /rest/api/3/fieldconfigurationscheme/project
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - projectId (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/fieldconfigurationscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_field_configuration_scheme_to_project(self, projectId: str, fieldConfigurationSchemeId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign field configuration scheme to project

HTTP PUT /rest/api/3/fieldconfigurationscheme/project
Body (application/json) fields:
  - fieldConfigurationSchemeId (str, optional)
  - projectId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if fieldConfigurationSchemeId is not None:
            _body['fieldConfigurationSchemeId'] = fieldConfigurationSchemeId
        _body['projectId'] = projectId
        rel_path = '/rest/api/3/fieldconfigurationscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_field_configuration_scheme(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete field configuration scheme

HTTP DELETE /rest/api/3/fieldconfigurationscheme/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/fieldconfigurationscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_field_configuration_scheme(self, id: int, name: str, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update field configuration scheme

HTTP PUT /rest/api/3/fieldconfigurationscheme/{id}
Path params:
  - id (int)
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        rel_path = '/rest/api/3/fieldconfigurationscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_field_configuration_scheme_mapping(self, id: int, mappings: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign issue types to field configurations

HTTP PUT /rest/api/3/fieldconfigurationscheme/{id}/mapping
Path params:
  - id (int)
Body (application/json) fields:
  - mappings (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['mappings'] = mappings
        rel_path = '/rest/api/3/fieldconfigurationscheme/{id}/mapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_issue_types_from_global_field_configuration_scheme(self, id: int, issueTypeIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove issue types from field configuration scheme

HTTP POST /rest/api/3/fieldconfigurationscheme/{id}/mapping/delete
Path params:
  - id (int)
Body (application/json) fields:
  - issueTypeIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeIds'] = issueTypeIds
        rel_path = '/rest/api/3/fieldconfigurationscheme/{id}/mapping/delete'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_filter(self, name: str, expand: Optional[str]=None, overrideSharePermissions: Optional[bool]=None, approximateLastUsed: Optional[str]=None, description: Optional[str]=None, editPermissions: Optional[list[Dict[str, Any]]]=None, favourite: Optional[bool]=None, favouritedCount: Optional[int]=None, id: Optional[str]=None, jql: Optional[str]=None, owner: Optional[Dict[str, Any]]=None, searchUrl: Optional[str]=None, self_: Optional[str]=None, sharePermissions: Optional[list[Dict[str, Any]]]=None, sharedUsers: Optional[Dict[str, Any]]=None, subscriptions: Optional[Dict[str, Any]]=None, viewUrl: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create filter

HTTP POST /rest/api/3/filter
Query params:
  - expand (str, optional)
  - overrideSharePermissions (bool, optional)
Body (application/json) fields:
  - approximateLastUsed (str, optional)
  - description (str, optional)
  - editPermissions (list[Dict[str, Any]], optional)
  - favourite (bool, optional)
  - favouritedCount (int, optional)
  - id (str, optional)
  - jql (str, optional)
  - name (str, required)
  - owner (Dict[str, Any], optional)
  - searchUrl (str, optional)
  - self (str, optional)
  - sharePermissions (list[Dict[str, Any]], optional)
  - sharedUsers (Dict[str, Any], optional)
  - subscriptions (Dict[str, Any], optional)
  - viewUrl (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if overrideSharePermissions is not None:
            _query['overrideSharePermissions'] = overrideSharePermissions
        _body: Dict[str, Any] = {}
        if approximateLastUsed is not None:
            _body['approximateLastUsed'] = approximateLastUsed
        if description is not None:
            _body['description'] = description
        if editPermissions is not None:
            _body['editPermissions'] = editPermissions
        if favourite is not None:
            _body['favourite'] = favourite
        if favouritedCount is not None:
            _body['favouritedCount'] = favouritedCount
        if id is not None:
            _body['id'] = id
        if jql is not None:
            _body['jql'] = jql
        _body['name'] = name
        if owner is not None:
            _body['owner'] = owner
        if searchUrl is not None:
            _body['searchUrl'] = searchUrl
        if self_ is not None:
            _body['self'] = self_
        if sharePermissions is not None:
            _body['sharePermissions'] = sharePermissions
        if sharedUsers is not None:
            _body['sharedUsers'] = sharedUsers
        if subscriptions is not None:
            _body['subscriptions'] = subscriptions
        if viewUrl is not None:
            _body['viewUrl'] = viewUrl
        rel_path = '/rest/api/3/filter'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_default_share_scope(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get default share scope

HTTP GET /rest/api/3/filter/defaultShareScope"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/defaultShareScope'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_default_share_scope(self, scope: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set default share scope

HTTP PUT /rest/api/3/filter/defaultShareScope
Body (application/json) fields:
  - scope (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['scope'] = scope
        rel_path = '/rest/api/3/filter/defaultShareScope'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_favourite_filters(self, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get favorite filters

HTTP GET /rest/api/3/filter/favourite
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/filter/favourite'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_my_filters(self, expand: Optional[str]=None, includeFavourites: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get my filters

HTTP GET /rest/api/3/filter/my
Query params:
  - expand (str, optional)
  - includeFavourites (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if includeFavourites is not None:
            _query['includeFavourites'] = includeFavourites
        _body = None
        rel_path = '/rest/api/3/filter/my'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_filters_paginated(self, filterName: Optional[str]=None, accountId: Optional[str]=None, owner: Optional[str]=None, groupname: Optional[str]=None, groupId: Optional[str]=None, projectId: Optional[int]=None, id: Optional[list[int]]=None, orderBy: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, expand: Optional[str]=None, overrideSharePermissions: Optional[bool]=None, isSubstringMatch: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search for filters

HTTP GET /rest/api/3/filter/search
Query params:
  - filterName (str, optional)
  - accountId (str, optional)
  - owner (str, optional)
  - groupname (str, optional)
  - groupId (str, optional)
  - projectId (int, optional)
  - id (list[int], optional)
  - orderBy (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - expand (str, optional)
  - overrideSharePermissions (bool, optional)
  - isSubstringMatch (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if filterName is not None:
            _query['filterName'] = filterName
        if accountId is not None:
            _query['accountId'] = accountId
        if owner is not None:
            _query['owner'] = owner
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        if projectId is not None:
            _query['projectId'] = projectId
        if id is not None:
            _query['id'] = id
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if expand is not None:
            _query['expand'] = expand
        if overrideSharePermissions is not None:
            _query['overrideSharePermissions'] = overrideSharePermissions
        if isSubstringMatch is not None:
            _query['isSubstringMatch'] = isSubstringMatch
        _body = None
        rel_path = '/rest/api/3/filter/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_filter(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete filter

HTTP DELETE /rest/api/3/filter/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_filter(self, id: int, expand: Optional[str]=None, overrideSharePermissions: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get filter

HTTP GET /rest/api/3/filter/{id}
Path params:
  - id (int)
Query params:
  - expand (str, optional)
  - overrideSharePermissions (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if overrideSharePermissions is not None:
            _query['overrideSharePermissions'] = overrideSharePermissions
        _body = None
        rel_path = '/rest/api/3/filter/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_filter(self, id: int, name: str, expand: Optional[str]=None, overrideSharePermissions: Optional[bool]=None, approximateLastUsed: Optional[str]=None, description: Optional[str]=None, editPermissions: Optional[list[Dict[str, Any]]]=None, favourite: Optional[bool]=None, favouritedCount: Optional[int]=None, id_body: Optional[str]=None, jql: Optional[str]=None, owner: Optional[Dict[str, Any]]=None, searchUrl: Optional[str]=None, self_: Optional[str]=None, sharePermissions: Optional[list[Dict[str, Any]]]=None, sharedUsers: Optional[Dict[str, Any]]=None, subscriptions: Optional[Dict[str, Any]]=None, viewUrl: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update filter

HTTP PUT /rest/api/3/filter/{id}
Path params:
  - id (int)
Query params:
  - expand (str, optional)
  - overrideSharePermissions (bool, optional)
Body (application/json) fields:
  - approximateLastUsed (str, optional)
  - description (str, optional)
  - editPermissions (list[Dict[str, Any]], optional)
  - favourite (bool, optional)
  - favouritedCount (int, optional)
  - id (str, optional)
  - jql (str, optional)
  - name (str, required)
  - owner (Dict[str, Any], optional)
  - searchUrl (str, optional)
  - self (str, optional)
  - sharePermissions (list[Dict[str, Any]], optional)
  - sharedUsers (Dict[str, Any], optional)
  - subscriptions (Dict[str, Any], optional)
  - viewUrl (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if overrideSharePermissions is not None:
            _query['overrideSharePermissions'] = overrideSharePermissions
        _body: Dict[str, Any] = {}
        if approximateLastUsed is not None:
            _body['approximateLastUsed'] = approximateLastUsed
        if description is not None:
            _body['description'] = description
        if editPermissions is not None:
            _body['editPermissions'] = editPermissions
        if favourite is not None:
            _body['favourite'] = favourite
        if favouritedCount is not None:
            _body['favouritedCount'] = favouritedCount
        if id_body is not None:
            _body['id'] = id_body
        if jql is not None:
            _body['jql'] = jql
        _body['name'] = name
        if owner is not None:
            _body['owner'] = owner
        if searchUrl is not None:
            _body['searchUrl'] = searchUrl
        if self_ is not None:
            _body['self'] = self_
        if sharePermissions is not None:
            _body['sharePermissions'] = sharePermissions
        if sharedUsers is not None:
            _body['sharedUsers'] = sharedUsers
        if subscriptions is not None:
            _body['subscriptions'] = subscriptions
        if viewUrl is not None:
            _body['viewUrl'] = viewUrl
        rel_path = '/rest/api/3/filter/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def reset_columns(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Reset columns

HTTP DELETE /rest/api/3/filter/{id}/columns
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/{id}/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_columns(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get columns

HTTP GET /rest/api/3/filter/{id}/columns
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/{id}/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_columns(self, id: int, columns: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set columns

HTTP PUT /rest/api/3/filter/{id}/columns
Path params:
  - id (int)
Body (application/json) fields:
  - columns (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if columns is not None:
            _body['columns'] = columns
        rel_path = '/rest/api/3/filter/{id}/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_favourite_for_filter(self, id: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove filter as favorite

HTTP DELETE /rest/api/3/filter/{id}/favourite
Path params:
  - id (int)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/filter/{id}/favourite'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_favourite_for_filter(self, id: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add filter as favorite

HTTP PUT /rest/api/3/filter/{id}/favourite
Path params:
  - id (int)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/filter/{id}/favourite'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def change_filter_owner(self, id: int, accountId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Change filter owner

HTTP PUT /rest/api/3/filter/{id}/owner
Path params:
  - id (int)
Body (application/json) fields:
  - accountId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['accountId'] = accountId
        rel_path = '/rest/api/3/filter/{id}/owner'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_share_permissions(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get share permissions

HTTP GET /rest/api/3/filter/{id}/permission
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/{id}/permission'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_share_permission(self, id: int, type: str, accountId: Optional[str]=None, groupId: Optional[str]=None, groupname: Optional[str]=None, projectId: Optional[str]=None, projectRoleId: Optional[str]=None, rights: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add share permission

HTTP POST /rest/api/3/filter/{id}/permission
Path params:
  - id (int)
Body (application/json) fields:
  - accountId (str, optional)
  - groupId (str, optional)
  - groupname (str, optional)
  - projectId (str, optional)
  - projectRoleId (str, optional)
  - rights (int, optional)
  - type (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if accountId is not None:
            _body['accountId'] = accountId
        if groupId is not None:
            _body['groupId'] = groupId
        if groupname is not None:
            _body['groupname'] = groupname
        if projectId is not None:
            _body['projectId'] = projectId
        if projectRoleId is not None:
            _body['projectRoleId'] = projectRoleId
        if rights is not None:
            _body['rights'] = rights
        _body['type'] = type
        rel_path = '/rest/api/3/filter/{id}/permission'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_share_permission(self, id: int, permissionId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete share permission

HTTP DELETE /rest/api/3/filter/{id}/permission/{permissionId}
Path params:
  - id (int)
  - permissionId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'permissionId': permissionId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/{id}/permission/{permissionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_share_permission(self, id: int, permissionId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get share permission

HTTP GET /rest/api/3/filter/{id}/permission/{permissionId}
Path params:
  - id (int)
  - permissionId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'permissionId': permissionId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/filter/{id}/permission/{permissionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_group(self, groupname: Optional[str]=None, groupId: Optional[str]=None, swapGroup: Optional[str]=None, swapGroupId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove group

HTTP DELETE /rest/api/3/group
Query params:
  - groupname (str, optional)
  - groupId (str, optional)
  - swapGroup (str, optional)
  - swapGroupId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        if swapGroup is not None:
            _query['swapGroup'] = swapGroup
        if swapGroupId is not None:
            _query['swapGroupId'] = swapGroupId
        _body = None
        rel_path = '/rest/api/3/group'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_group(self, groupname: Optional[str]=None, groupId: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get group

HTTP GET /rest/api/3/group
Query params:
  - groupname (str, optional)
  - groupId (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/group'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_group(self, name: str, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create group

HTTP POST /rest/api/3/group
Body (application/json) fields:
  - name (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/group'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_get_groups(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, groupId: Optional[list[str]]=None, groupName: Optional[list[str]]=None, accessType: Optional[str]=None, applicationKey: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk get groups

HTTP GET /rest/api/3/group/bulk
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - groupId (list[str], optional)
  - groupName (list[str], optional)
  - accessType (str, optional)
  - applicationKey (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if groupId is not None:
            _query['groupId'] = groupId
        if groupName is not None:
            _query['groupName'] = groupName
        if accessType is not None:
            _query['accessType'] = accessType
        if applicationKey is not None:
            _query['applicationKey'] = applicationKey
        _body = None
        rel_path = '/rest/api/3/group/bulk'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_users_from_group(self, groupname: Optional[str]=None, groupId: Optional[str]=None, includeInactiveUsers: Optional[bool]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get users from group

HTTP GET /rest/api/3/group/member
Query params:
  - groupname (str, optional)
  - groupId (str, optional)
  - includeInactiveUsers (bool, optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        if includeInactiveUsers is not None:
            _query['includeInactiveUsers'] = includeInactiveUsers
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/group/member'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_user_from_group(self, accountId: str, groupname: Optional[str]=None, groupId: Optional[str]=None, username: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove user from group

HTTP DELETE /rest/api/3/group/user
Query params:
  - groupname (str, optional)
  - groupId (str, optional)
  - username (str, optional)
  - accountId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        if username is not None:
            _query['username'] = username
        _query['accountId'] = accountId
        _body = None
        rel_path = '/rest/api/3/group/user'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_user_to_group(self, groupname: Optional[str]=None, groupId: Optional[str]=None, accountId: Optional[str]=None, name: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add user to group

HTTP POST /rest/api/3/group/user
Query params:
  - groupname (str, optional)
  - groupId (str, optional)
Body (application/json) fields:
  - accountId (str, optional)
  - name (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if groupname is not None:
            _query['groupname'] = groupname
        if groupId is not None:
            _query['groupId'] = groupId
        _body: Dict[str, Any] = {}
        if accountId is not None:
            _body['accountId'] = accountId
        if name is not None:
            _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/group/user'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_groups(self, accountId: Optional[str]=None, query: Optional[str]=None, exclude: Optional[list[str]]=None, excludeId: Optional[list[str]]=None, maxResults: Optional[int]=None, caseInsensitive: Optional[bool]=None, userName: Optional[str]=None, includeTeams: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find groups

HTTP GET /rest/api/3/groups/picker
Query params:
  - accountId (str, optional)
  - query (str, optional)
  - exclude (list[str], optional)
  - excludeId (list[str], optional)
  - maxResults (int, optional)
  - caseInsensitive (bool, optional)
  - userName (str, optional)
  - includeTeams (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if query is not None:
            _query['query'] = query
        if exclude is not None:
            _query['exclude'] = exclude
        if excludeId is not None:
            _query['excludeId'] = excludeId
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if caseInsensitive is not None:
            _query['caseInsensitive'] = caseInsensitive
        if userName is not None:
            _query['userName'] = userName
        if includeTeams is not None:
            _query['includeTeams'] = includeTeams
        _body = None
        rel_path = '/rest/api/3/groups/picker'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_users_and_groups(self, query: str, maxResults: Optional[int]=None, showAvatar: Optional[bool]=None, fieldId: Optional[str]=None, projectId: Optional[list[str]]=None, issueTypeId: Optional[list[str]]=None, avatarSize: Optional[str]=None, caseInsensitive: Optional[bool]=None, excludeConnectAddons: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users and groups

HTTP GET /rest/api/3/groupuserpicker
Query params:
  - query (str, required)
  - maxResults (int, optional)
  - showAvatar (bool, optional)
  - fieldId (str, optional)
  - projectId (list[str], optional)
  - issueTypeId (list[str], optional)
  - avatarSize (str, optional)
  - caseInsensitive (bool, optional)
  - excludeConnectAddons (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['query'] = query
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if showAvatar is not None:
            _query['showAvatar'] = showAvatar
        if fieldId is not None:
            _query['fieldId'] = fieldId
        if projectId is not None:
            _query['projectId'] = projectId
        if issueTypeId is not None:
            _query['issueTypeId'] = issueTypeId
        if avatarSize is not None:
            _query['avatarSize'] = avatarSize
        if caseInsensitive is not None:
            _query['caseInsensitive'] = caseInsensitive
        if excludeConnectAddons is not None:
            _query['excludeConnectAddons'] = excludeConnectAddons
        _body = None
        rel_path = '/rest/api/3/groupuserpicker'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_license(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get license

HTTP GET /rest/api/3/instance/license"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/instance/license'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue(self, updateHistory: Optional[bool]=None, fields: Optional[Dict[str, Any]]=None, historyMetadata: Optional[Dict[str, Any]]=None, properties: Optional[list[Dict[str, Any]]]=None, transition: Optional[Dict[str, Any]]=None, update: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue

HTTP POST /rest/api/3/issue
Query params:
  - updateHistory (bool, optional)
Body (application/json) fields:
  - fields (Dict[str, Any], optional)
  - historyMetadata (Dict[str, Any], optional)
  - properties (list[Dict[str, Any]], optional)
  - transition (Dict[str, Any], optional)
  - update (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if updateHistory is not None:
            _query['updateHistory'] = updateHistory
        _body: Dict[str, Any] = {}
        if fields is not None:
            _body['fields'] = fields
        if historyMetadata is not None:
            _body['historyMetadata'] = historyMetadata
        if properties is not None:
            _body['properties'] = properties
        if transition is not None:
            _body['transition'] = transition
        if update is not None:
            _body['update'] = update
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def archive_issues_async(self, jql: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Archive issue(s) by JQL

HTTP POST /rest/api/3/issue/archive
Body (application/json) fields:
  - jql (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if jql is not None:
            _body['jql'] = jql
        rel_path = '/rest/api/3/issue/archive'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def archive_issues(self, issueIdsOrKeys: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Archive issue(s) by issue ID/key

HTTP PUT /rest/api/3/issue/archive
Body (application/json) fields:
  - issueIdsOrKeys (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issueIdsOrKeys is not None:
            _body['issueIdsOrKeys'] = issueIdsOrKeys
        rel_path = '/rest/api/3/issue/archive'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issues(self, issueUpdates: Optional[list[Dict[str, Any]]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk create issue

HTTP POST /rest/api/3/issue/bulk
Body (application/json) fields:
  - issueUpdates (list[Dict[str, Any]], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issueUpdates is not None:
            _body['issueUpdates'] = issueUpdates
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/bulk'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_fetch_issues(self, issueIdsOrKeys: list[str], expand: Optional[list[str]]=None, fields: Optional[list[str]]=None, fieldsByKeys: Optional[bool]=None, properties: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk fetch issues

HTTP POST /rest/api/3/issue/bulkfetch
Body (application/json) fields:
  - expand (list[str], optional)
  - fields (list[str], optional)
  - fieldsByKeys (bool, optional)
  - issueIdsOrKeys (list[str], required)
  - properties (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if expand is not None:
            _body['expand'] = expand
        if fields is not None:
            _body['fields'] = fields
        if fieldsByKeys is not None:
            _body['fieldsByKeys'] = fieldsByKeys
        _body['issueIdsOrKeys'] = issueIdsOrKeys
        if properties is not None:
            _body['properties'] = properties
        rel_path = '/rest/api/3/issue/bulkfetch'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_create_issue_meta(self, projectIds: Optional[list[str]]=None, projectKeys: Optional[list[str]]=None, issuetypeIds: Optional[list[str]]=None, issuetypeNames: Optional[list[str]]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get create issue metadata

HTTP GET /rest/api/3/issue/createmeta
Query params:
  - projectIds (list[str], optional)
  - projectKeys (list[str], optional)
  - issuetypeIds (list[str], optional)
  - issuetypeNames (list[str], optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if projectIds is not None:
            _query['projectIds'] = projectIds
        if projectKeys is not None:
            _query['projectKeys'] = projectKeys
        if issuetypeIds is not None:
            _query['issuetypeIds'] = issuetypeIds
        if issuetypeNames is not None:
            _query['issuetypeNames'] = issuetypeNames
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issue/createmeta'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_create_issue_meta_issue_types(self, projectIdOrKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get create metadata issue types for a project

HTTP GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes
Path params:
  - projectIdOrKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_create_issue_meta_issue_type_id(self, projectIdOrKey: str, issueTypeId: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get create field metadata for a project and issue type id

HTTP GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}
Path params:
  - projectIdOrKey (str)
  - issueTypeId (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'issueTypeId': issueTypeId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_limit_report(self, isReturningKeys: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue limit report

HTTP GET /rest/api/3/issue/limit/report
Query params:
  - isReturningKeys (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if isReturningKeys is not None:
            _query['isReturningKeys'] = isReturningKeys
        _body = None
        rel_path = '/rest/api/3/issue/limit/report'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_picker_resource(self, query: Optional[str]=None, currentJQL: Optional[str]=None, currentIssueKey: Optional[str]=None, currentProjectId: Optional[str]=None, showSubTasks: Optional[bool]=None, showSubTaskParent: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue picker suggestions

HTTP GET /rest/api/3/issue/picker
Query params:
  - query (str, optional)
  - currentJQL (str, optional)
  - currentIssueKey (str, optional)
  - currentProjectId (str, optional)
  - showSubTasks (bool, optional)
  - showSubTaskParent (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if query is not None:
            _query['query'] = query
        if currentJQL is not None:
            _query['currentJQL'] = currentJQL
        if currentIssueKey is not None:
            _query['currentIssueKey'] = currentIssueKey
        if currentProjectId is not None:
            _query['currentProjectId'] = currentProjectId
        if showSubTasks is not None:
            _query['showSubTasks'] = showSubTasks
        if showSubTaskParent is not None:
            _query['showSubTaskParent'] = showSubTaskParent
        _body = None
        rel_path = '/rest/api/3/issue/picker'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_set_issues_properties_list(self, entitiesIds: Optional[list[int]]=None, properties: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk set issues properties by list

HTTP POST /rest/api/3/issue/properties
Body (application/json) fields:
  - entitiesIds (list[int], optional)
  - properties (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if entitiesIds is not None:
            _body['entitiesIds'] = entitiesIds
        if properties is not None:
            _body['properties'] = properties
        rel_path = '/rest/api/3/issue/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_set_issue_properties_by_issue(self, issues: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk set issue properties by issue

HTTP POST /rest/api/3/issue/properties/multi
Body (application/json) fields:
  - issues (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issues is not None:
            _body['issues'] = issues
        rel_path = '/rest/api/3/issue/properties/multi'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_delete_issue_property(self, propertyKey: str, currentValue: Optional[str]=None, entityIds: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk delete issue property

HTTP DELETE /rest/api/3/issue/properties/{propertyKey}
Path params:
  - propertyKey (str)
Body (application/json) fields:
  - currentValue (str, optional)
  - entityIds (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if currentValue is not None:
            _body['currentValue'] = currentValue
        if entityIds is not None:
            _body['entityIds'] = entityIds
        rel_path = '/rest/api/3/issue/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_set_issue_property(self, propertyKey: str, expression: Optional[str]=None, filter: Optional[Dict[str, Any]]=None, value: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk set issue property

HTTP PUT /rest/api/3/issue/properties/{propertyKey}
Path params:
  - propertyKey (str)
Body (application/json) fields:
  - expression (str, optional)
  - filter (Dict[str, Any], optional)
  - value (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if expression is not None:
            _body['expression'] = expression
        if filter is not None:
            _body['filter'] = filter
        if value is not None:
            _body['value'] = value
        rel_path = '/rest/api/3/issue/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def unarchive_issues(self, issueIdsOrKeys: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Unarchive issue(s) by issue keys/ID

HTTP PUT /rest/api/3/issue/unarchive
Body (application/json) fields:
  - issueIdsOrKeys (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issueIdsOrKeys is not None:
            _body['issueIdsOrKeys'] = issueIdsOrKeys
        rel_path = '/rest/api/3/issue/unarchive'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_is_watching_issue_bulk(self, issueIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get is watching issue bulk

HTTP POST /rest/api/3/issue/watching
Body (application/json) fields:
  - issueIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueIds'] = issueIds
        rel_path = '/rest/api/3/issue/watching'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue(self, issueIdOrKey: str, deleteSubtasks: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}
Path params:
  - issueIdOrKey (str)
Query params:
  - deleteSubtasks (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if deleteSubtasks is not None:
            _query['deleteSubtasks'] = deleteSubtasks
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue(self, issueIdOrKey: str, fields: Optional[list[str]]=None, fieldsByKeys: Optional[bool]=None, expand: Optional[str]=None, properties: Optional[list[str]]=None, updateHistory: Optional[bool]=None, failFast: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue

HTTP GET /rest/api/3/issue/{issueIdOrKey}
Path params:
  - issueIdOrKey (str)
Query params:
  - fields (list[str], optional)
  - fieldsByKeys (bool, optional)
  - expand (str, optional)
  - properties (list[str], optional)
  - updateHistory (bool, optional)
  - failFast (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if fields is not None:
            _query['fields'] = fields
        if fieldsByKeys is not None:
            _query['fieldsByKeys'] = fieldsByKeys
        if expand is not None:
            _query['expand'] = expand
        if properties is not None:
            _query['properties'] = properties
        if updateHistory is not None:
            _query['updateHistory'] = updateHistory
        if failFast is not None:
            _query['failFast'] = failFast
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def edit_issue(self, issueIdOrKey: str, notifyUsers: Optional[bool]=None, overrideScreenSecurity: Optional[bool]=None, overrideEditableFlag: Optional[bool]=None, returnIssue: Optional[bool]=None, expand: Optional[str]=None, fields: Optional[Dict[str, Any]]=None, historyMetadata: Optional[Dict[str, Any]]=None, properties: Optional[list[Dict[str, Any]]]=None, transition: Optional[Dict[str, Any]]=None, update: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Edit issue

HTTP PUT /rest/api/3/issue/{issueIdOrKey}
Path params:
  - issueIdOrKey (str)
Query params:
  - notifyUsers (bool, optional)
  - overrideScreenSecurity (bool, optional)
  - overrideEditableFlag (bool, optional)
  - returnIssue (bool, optional)
  - expand (str, optional)
Body (application/json) fields:
  - fields (Dict[str, Any], optional)
  - historyMetadata (Dict[str, Any], optional)
  - properties (list[Dict[str, Any]], optional)
  - transition (Dict[str, Any], optional)
  - update (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if notifyUsers is not None:
            _query['notifyUsers'] = notifyUsers
        if overrideScreenSecurity is not None:
            _query['overrideScreenSecurity'] = overrideScreenSecurity
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        if returnIssue is not None:
            _query['returnIssue'] = returnIssue
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if fields is not None:
            _body['fields'] = fields
        if historyMetadata is not None:
            _body['historyMetadata'] = historyMetadata
        if properties is not None:
            _body['properties'] = properties
        if transition is not None:
            _body['transition'] = transition
        if update is not None:
            _body['update'] = update
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_issue(self, issueIdOrKey: str, accountId: Optional[str]=None, accountType: Optional[str]=None, active: Optional[bool]=None, applicationRoles: Optional[Dict[str, Any]]=None, avatarUrls: Optional[Dict[str, Any]]=None, displayName: Optional[str]=None, emailAddress: Optional[str]=None, expand: Optional[str]=None, groups: Optional[Dict[str, Any]]=None, key: Optional[str]=None, locale: Optional[str]=None, name: Optional[str]=None, self_: Optional[str]=None, timeZone: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign issue

HTTP PUT /rest/api/3/issue/{issueIdOrKey}/assignee
Path params:
  - issueIdOrKey (str)
Body (application/json) fields:
  - accountId (str, optional)
  - accountType (str, optional)
  - active (bool, optional)
  - applicationRoles (Dict[str, Any], optional)
  - avatarUrls (Dict[str, Any], optional)
  - displayName (str, optional)
  - emailAddress (str, optional)
  - expand (str, optional)
  - groups (Dict[str, Any], optional)
  - key (str, optional)
  - locale (str, optional)
  - name (str, optional)
  - self (str, optional)
  - timeZone (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if accountId is not None:
            _body['accountId'] = accountId
        if accountType is not None:
            _body['accountType'] = accountType
        if active is not None:
            _body['active'] = active
        if applicationRoles is not None:
            _body['applicationRoles'] = applicationRoles
        if avatarUrls is not None:
            _body['avatarUrls'] = avatarUrls
        if displayName is not None:
            _body['displayName'] = displayName
        if emailAddress is not None:
            _body['emailAddress'] = emailAddress
        if expand is not None:
            _body['expand'] = expand
        if groups is not None:
            _body['groups'] = groups
        if key is not None:
            _body['key'] = key
        if locale is not None:
            _body['locale'] = locale
        if name is not None:
            _body['name'] = name
        if self_ is not None:
            _body['self'] = self_
        if timeZone is not None:
            _body['timeZone'] = timeZone
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/assignee'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_attachment(self, issueIdOrKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add attachment

HTTP POST /rest/api/3/issue/{issueIdOrKey}/attachments
Path params:
  - issueIdOrKey (str)
Body: multipart/form-data (list[Dict[str, Any]])"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'multipart/form-data')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/attachments'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_change_logs(self, issueIdOrKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get changelogs

HTTP GET /rest/api/3/issue/{issueIdOrKey}/changelog
Path params:
  - issueIdOrKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/changelog'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_change_logs_by_ids(self, issueIdOrKey: str, changelogIds: list[int], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get changelogs by IDs

HTTP POST /rest/api/3/issue/{issueIdOrKey}/changelog/list
Path params:
  - issueIdOrKey (str)
Body (application/json) fields:
  - changelogIds (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['changelogIds'] = changelogIds
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/changelog/list'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_comments(self, issueIdOrKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, orderBy: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get comments

HTTP GET /rest/api/3/issue/{issueIdOrKey}/comment
Path params:
  - issueIdOrKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - orderBy (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/comment'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_comment(self, issueIdOrKey: str, expand: Optional[str]=None, author: Optional[Dict[str, Any]]=None, body_body: Optional[str]=None, created: Optional[str]=None, id: Optional[str]=None, jsdAuthorCanSeeRequest: Optional[bool]=None, jsdPublic: Optional[bool]=None, properties: Optional[list[Dict[str, Any]]]=None, renderedBody: Optional[str]=None, self_: Optional[str]=None, updateAuthor: Optional[Dict[str, Any]]=None, updated: Optional[str]=None, visibility: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add comment

HTTP POST /rest/api/3/issue/{issueIdOrKey}/comment
Path params:
  - issueIdOrKey (str)
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - author (Dict[str, Any], optional)
  - body (str, optional)
  - created (str, optional)
  - id (str, optional)
  - jsdAuthorCanSeeRequest (bool, optional)
  - jsdPublic (bool, optional)
  - properties (list[Dict[str, Any]], optional)
  - renderedBody (str, optional)
  - self (str, optional)
  - updateAuthor (Dict[str, Any], optional)
  - updated (str, optional)
  - visibility (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if author is not None:
            _body['author'] = author
        if body_body is not None:
            _body['body'] = body_body
        if created is not None:
            _body['created'] = created
        if id is not None:
            _body['id'] = id
        if jsdAuthorCanSeeRequest is not None:
            _body['jsdAuthorCanSeeRequest'] = jsdAuthorCanSeeRequest
        if jsdPublic is not None:
            _body['jsdPublic'] = jsdPublic
        if properties is not None:
            _body['properties'] = properties
        if renderedBody is not None:
            _body['renderedBody'] = renderedBody
        if self_ is not None:
            _body['self'] = self_
        if updateAuthor is not None:
            _body['updateAuthor'] = updateAuthor
        if updated is not None:
            _body['updated'] = updated
        if visibility is not None:
            _body['visibility'] = visibility
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/comment'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_comment(self, issueIdOrKey: str, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete comment

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id}
Path params:
  - issueIdOrKey (str)
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/comment/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_comment(self, issueIdOrKey: str, id: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get comment

HTTP GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}
Path params:
  - issueIdOrKey (str)
  - id (str)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/comment/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_comment(self, issueIdOrKey: str, id: str, notifyUsers: Optional[bool]=None, overrideEditableFlag: Optional[bool]=None, expand: Optional[str]=None, author: Optional[Dict[str, Any]]=None, body_body: Optional[str]=None, created: Optional[str]=None, id_body: Optional[str]=None, jsdAuthorCanSeeRequest: Optional[bool]=None, jsdPublic: Optional[bool]=None, properties: Optional[list[Dict[str, Any]]]=None, renderedBody: Optional[str]=None, self_: Optional[str]=None, updateAuthor: Optional[Dict[str, Any]]=None, updated: Optional[str]=None, visibility: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update comment

HTTP PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}
Path params:
  - issueIdOrKey (str)
  - id (str)
Query params:
  - notifyUsers (bool, optional)
  - overrideEditableFlag (bool, optional)
  - expand (str, optional)
Body (application/json) fields:
  - author (Dict[str, Any], optional)
  - body (str, optional)
  - created (str, optional)
  - id (str, optional)
  - jsdAuthorCanSeeRequest (bool, optional)
  - jsdPublic (bool, optional)
  - properties (list[Dict[str, Any]], optional)
  - renderedBody (str, optional)
  - self (str, optional)
  - updateAuthor (Dict[str, Any], optional)
  - updated (str, optional)
  - visibility (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if notifyUsers is not None:
            _query['notifyUsers'] = notifyUsers
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if author is not None:
            _body['author'] = author
        if body_body is not None:
            _body['body'] = body_body
        if created is not None:
            _body['created'] = created
        if id_body is not None:
            _body['id'] = id_body
        if jsdAuthorCanSeeRequest is not None:
            _body['jsdAuthorCanSeeRequest'] = jsdAuthorCanSeeRequest
        if jsdPublic is not None:
            _body['jsdPublic'] = jsdPublic
        if properties is not None:
            _body['properties'] = properties
        if renderedBody is not None:
            _body['renderedBody'] = renderedBody
        if self_ is not None:
            _body['self'] = self_
        if updateAuthor is not None:
            _body['updateAuthor'] = updateAuthor
        if updated is not None:
            _body['updated'] = updated
        if visibility is not None:
            _body['visibility'] = visibility
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/comment/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_edit_issue_meta(self, issueIdOrKey: str, overrideScreenSecurity: Optional[bool]=None, overrideEditableFlag: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get edit issue metadata

HTTP GET /rest/api/3/issue/{issueIdOrKey}/editmeta
Path params:
  - issueIdOrKey (str)
Query params:
  - overrideScreenSecurity (bool, optional)
  - overrideEditableFlag (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if overrideScreenSecurity is not None:
            _query['overrideScreenSecurity'] = overrideScreenSecurity
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/editmeta'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def notify(self, issueIdOrKey: str, htmlBody: Optional[str]=None, restrict: Optional[Dict[str, Any]]=None, subject: Optional[str]=None, textBody: Optional[str]=None, to: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Send notification for issue

HTTP POST /rest/api/3/issue/{issueIdOrKey}/notify
Path params:
  - issueIdOrKey (str)
Body (application/json) fields:
  - htmlBody (str, optional)
  - restrict (Dict[str, Any], optional)
  - subject (str, optional)
  - textBody (str, optional)
  - to (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if htmlBody is not None:
            _body['htmlBody'] = htmlBody
        if restrict is not None:
            _body['restrict'] = restrict
        if subject is not None:
            _body['subject'] = subject
        if textBody is not None:
            _body['textBody'] = textBody
        if to is not None:
            _body['to'] = to
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/notify'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_property_keys(self, issueIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue property keys

HTTP GET /rest/api/3/issue/{issueIdOrKey}/properties
Path params:
  - issueIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    @codeflash_performance_async
    async def delete_issue_property(self, issueIdOrKey: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue property

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}
Path params:
  - issueIdOrKey (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_property(self, issueIdOrKey: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue property

HTTP GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}
Path params:
  - issueIdOrKey (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_issue_property(self, issueIdOrKey: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set issue property

HTTP PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}
Path params:
  - issueIdOrKey (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_remote_issue_link_by_global_id(self, issueIdOrKey: str, globalId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete remote issue link by global ID

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink
Path params:
  - issueIdOrKey (str)
Query params:
  - globalId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _query['globalId'] = globalId
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/remotelink'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_remote_issue_links(self, issueIdOrKey: str, globalId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get remote issue links

HTTP GET /rest/api/3/issue/{issueIdOrKey}/remotelink
Path params:
  - issueIdOrKey (str)
Query params:
  - globalId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if globalId is not None:
            _query['globalId'] = globalId
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/remotelink'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_or_update_remote_issue_link(self, issueIdOrKey: str, object: Dict[str, Any], application: Optional[Dict[str, Any]]=None, globalId: Optional[str]=None, relationship: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create or update remote issue link

HTTP POST /rest/api/3/issue/{issueIdOrKey}/remotelink
Path params:
  - issueIdOrKey (str)
Body (application/json) fields:
  - application (Dict[str, Any], optional)
  - globalId (str, optional)
  - object (Dict[str, Any], required)
  - relationship (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if application is not None:
            _body['application'] = application
        if globalId is not None:
            _body['globalId'] = globalId
        _body['object'] = object
        if relationship is not None:
            _body['relationship'] = relationship
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/remotelink'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_remote_issue_link_by_id(self, issueIdOrKey: str, linkId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete remote issue link by ID

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}
Path params:
  - issueIdOrKey (str)
  - linkId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'linkId': linkId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_remote_issue_link_by_id(self, issueIdOrKey: str, linkId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get remote issue link by ID

HTTP GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}
Path params:
  - issueIdOrKey (str)
  - linkId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'linkId': linkId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_remote_issue_link(self, issueIdOrKey: str, linkId: str, object: Dict[str, Any], application: Optional[Dict[str, Any]]=None, globalId: Optional[str]=None, relationship: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update remote issue link by ID

HTTP PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}
Path params:
  - issueIdOrKey (str)
  - linkId (str)
Body (application/json) fields:
  - application (Dict[str, Any], optional)
  - globalId (str, optional)
  - object (Dict[str, Any], required)
  - relationship (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'linkId': linkId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if application is not None:
            _body['application'] = application
        if globalId is not None:
            _body['globalId'] = globalId
        _body['object'] = object
        if relationship is not None:
            _body['relationship'] = relationship
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_transitions(self, issueIdOrKey: str, expand: Optional[str]=None, transitionId: Optional[str]=None, skipRemoteOnlyCondition: Optional[bool]=None, includeUnavailableTransitions: Optional[bool]=None, sortByOpsBarAndStatus: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get transitions

HTTP GET /rest/api/3/issue/{issueIdOrKey}/transitions
Path params:
  - issueIdOrKey (str)
Query params:
  - expand (str, optional)
  - transitionId (str, optional)
  - skipRemoteOnlyCondition (bool, optional)
  - includeUnavailableTransitions (bool, optional)
  - sortByOpsBarAndStatus (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if transitionId is not None:
            _query['transitionId'] = transitionId
        if skipRemoteOnlyCondition is not None:
            _query['skipRemoteOnlyCondition'] = skipRemoteOnlyCondition
        if includeUnavailableTransitions is not None:
            _query['includeUnavailableTransitions'] = includeUnavailableTransitions
        if sortByOpsBarAndStatus is not None:
            _query['sortByOpsBarAndStatus'] = sortByOpsBarAndStatus
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/transitions'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def do_transition(self, issueIdOrKey: str, fields: Optional[Dict[str, Any]]=None, historyMetadata: Optional[Dict[str, Any]]=None, properties: Optional[list[Dict[str, Any]]]=None, transition: Optional[Dict[str, Any]]=None, update: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Transition issue

HTTP POST /rest/api/3/issue/{issueIdOrKey}/transitions
Path params:
  - issueIdOrKey (str)
Body (application/json) fields:
  - fields (Dict[str, Any], optional)
  - historyMetadata (Dict[str, Any], optional)
  - properties (list[Dict[str, Any]], optional)
  - transition (Dict[str, Any], optional)
  - update (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if fields is not None:
            _body['fields'] = fields
        if historyMetadata is not None:
            _body['historyMetadata'] = historyMetadata
        if properties is not None:
            _body['properties'] = properties
        if transition is not None:
            _body['transition'] = transition
        if update is not None:
            _body['update'] = update
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/transitions'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_vote(self, issueIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete vote

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/votes
Path params:
  - issueIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/votes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_votes(self, issueIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get votes

HTTP GET /rest/api/3/issue/{issueIdOrKey}/votes
Path params:
  - issueIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/votes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_vote(self, issueIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add vote

HTTP POST /rest/api/3/issue/{issueIdOrKey}/votes
Path params:
  - issueIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/votes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_watcher(self, issueIdOrKey: str, username: Optional[str]=None, accountId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete watcher

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/watchers
Path params:
  - issueIdOrKey (str)
Query params:
  - username (str, optional)
  - accountId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if username is not None:
            _query['username'] = username
        if accountId is not None:
            _query['accountId'] = accountId
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/watchers'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_watchers(self, issueIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue watchers

HTTP GET /rest/api/3/issue/{issueIdOrKey}/watchers
Path params:
  - issueIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/watchers'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_watcher(self, issueIdOrKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add watcher

HTTP POST /rest/api/3/issue/{issueIdOrKey}/watchers
Path params:
  - issueIdOrKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/watchers'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_delete_worklogs(self, issueIdOrKey: str, ids: list[int], adjustEstimate: Optional[str]=None, overrideEditableFlag: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk delete worklogs

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/worklog
Path params:
  - issueIdOrKey (str)
Query params:
  - adjustEstimate (str, optional)
  - overrideEditableFlag (bool, optional)
Body (application/json) fields:
  - ids (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if adjustEstimate is not None:
            _query['adjustEstimate'] = adjustEstimate
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body: Dict[str, Any] = {}
        _body['ids'] = ids
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_worklog(self, issueIdOrKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, startedAfter: Optional[int]=None, startedBefore: Optional[int]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue worklogs

HTTP GET /rest/api/3/issue/{issueIdOrKey}/worklog
Path params:
  - issueIdOrKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - startedAfter (int, optional)
  - startedBefore (int, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if startedAfter is not None:
            _query['startedAfter'] = startedAfter
        if startedBefore is not None:
            _query['startedBefore'] = startedBefore
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_worklog(self, issueIdOrKey: str, notifyUsers: Optional[bool]=None, adjustEstimate: Optional[str]=None, newEstimate: Optional[str]=None, reduceBy: Optional[str]=None, expand: Optional[str]=None, overrideEditableFlag: Optional[bool]=None, author: Optional[Dict[str, Any]]=None, comment: Optional[str]=None, created: Optional[str]=None, id: Optional[str]=None, issueId: Optional[str]=None, properties: Optional[list[Dict[str, Any]]]=None, self_: Optional[str]=None, started: Optional[str]=None, timeSpent: Optional[str]=None, timeSpentSeconds: Optional[int]=None, updateAuthor: Optional[Dict[str, Any]]=None, updated: Optional[str]=None, visibility: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add worklog

HTTP POST /rest/api/3/issue/{issueIdOrKey}/worklog
Path params:
  - issueIdOrKey (str)
Query params:
  - notifyUsers (bool, optional)
  - adjustEstimate (str, optional)
  - newEstimate (str, optional)
  - reduceBy (str, optional)
  - expand (str, optional)
  - overrideEditableFlag (bool, optional)
Body (application/json) fields:
  - author (Dict[str, Any], optional)
  - comment (str, optional)
  - created (str, optional)
  - id (str, optional)
  - issueId (str, optional)
  - properties (list[Dict[str, Any]], optional)
  - self (str, optional)
  - started (str, optional)
  - timeSpent (str, optional)
  - timeSpentSeconds (int, optional)
  - updateAuthor (Dict[str, Any], optional)
  - updated (str, optional)
  - visibility (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if notifyUsers is not None:
            _query['notifyUsers'] = notifyUsers
        if adjustEstimate is not None:
            _query['adjustEstimate'] = adjustEstimate
        if newEstimate is not None:
            _query['newEstimate'] = newEstimate
        if reduceBy is not None:
            _query['reduceBy'] = reduceBy
        if expand is not None:
            _query['expand'] = expand
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body: Dict[str, Any] = {}
        if author is not None:
            _body['author'] = author
        if comment is not None:
            _body['comment'] = comment
        if created is not None:
            _body['created'] = created
        if id is not None:
            _body['id'] = id
        if issueId is not None:
            _body['issueId'] = issueId
        if properties is not None:
            _body['properties'] = properties
        if self_ is not None:
            _body['self'] = self_
        if started is not None:
            _body['started'] = started
        if timeSpent is not None:
            _body['timeSpent'] = timeSpent
        if timeSpentSeconds is not None:
            _body['timeSpentSeconds'] = timeSpentSeconds
        if updateAuthor is not None:
            _body['updateAuthor'] = updateAuthor
        if updated is not None:
            _body['updated'] = updated
        if visibility is not None:
            _body['visibility'] = visibility
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_move_worklogs(self, issueIdOrKey: str, adjustEstimate: Optional[str]=None, overrideEditableFlag: Optional[bool]=None, ids: Optional[list[int]]=None, issueIdOrKey_body: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk move worklogs

HTTP POST /rest/api/3/issue/{issueIdOrKey}/worklog/move
Path params:
  - issueIdOrKey (str)
Query params:
  - adjustEstimate (str, optional)
  - overrideEditableFlag (bool, optional)
Body (application/json) fields:
  - ids (list[int], optional)
  - issueIdOrKey (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey}
        _query: Dict[str, Any] = {}
        if adjustEstimate is not None:
            _query['adjustEstimate'] = adjustEstimate
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body: Dict[str, Any] = {}
        if ids is not None:
            _body['ids'] = ids
        if issueIdOrKey_body is not None:
            _body['issueIdOrKey'] = issueIdOrKey_body
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_worklog(self, issueIdOrKey: str, id: str, notifyUsers: Optional[bool]=None, adjustEstimate: Optional[str]=None, newEstimate: Optional[str]=None, increaseBy: Optional[str]=None, overrideEditableFlag: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete worklog

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id}
Path params:
  - issueIdOrKey (str)
  - id (str)
Query params:
  - notifyUsers (bool, optional)
  - adjustEstimate (str, optional)
  - newEstimate (str, optional)
  - increaseBy (str, optional)
  - overrideEditableFlag (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if notifyUsers is not None:
            _query['notifyUsers'] = notifyUsers
        if adjustEstimate is not None:
            _query['adjustEstimate'] = adjustEstimate
        if newEstimate is not None:
            _query['newEstimate'] = newEstimate
        if increaseBy is not None:
            _query['increaseBy'] = increaseBy
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_worklog(self, issueIdOrKey: str, id: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get worklog

HTTP GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}
Path params:
  - issueIdOrKey (str)
  - id (str)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_worklog(self, issueIdOrKey: str, id: str, notifyUsers: Optional[bool]=None, adjustEstimate: Optional[str]=None, newEstimate: Optional[str]=None, expand: Optional[str]=None, overrideEditableFlag: Optional[bool]=None, author: Optional[Dict[str, Any]]=None, comment: Optional[str]=None, created: Optional[str]=None, id_body: Optional[str]=None, issueId: Optional[str]=None, properties: Optional[list[Dict[str, Any]]]=None, self_: Optional[str]=None, started: Optional[str]=None, timeSpent: Optional[str]=None, timeSpentSeconds: Optional[int]=None, updateAuthor: Optional[Dict[str, Any]]=None, updated: Optional[str]=None, visibility: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update worklog

HTTP PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}
Path params:
  - issueIdOrKey (str)
  - id (str)
Query params:
  - notifyUsers (bool, optional)
  - adjustEstimate (str, optional)
  - newEstimate (str, optional)
  - expand (str, optional)
  - overrideEditableFlag (bool, optional)
Body (application/json) fields:
  - author (Dict[str, Any], optional)
  - comment (str, optional)
  - created (str, optional)
  - id (str, optional)
  - issueId (str, optional)
  - properties (list[Dict[str, Any]], optional)
  - self (str, optional)
  - started (str, optional)
  - timeSpent (str, optional)
  - timeSpentSeconds (int, optional)
  - updateAuthor (Dict[str, Any], optional)
  - updated (str, optional)
  - visibility (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if notifyUsers is not None:
            _query['notifyUsers'] = notifyUsers
        if adjustEstimate is not None:
            _query['adjustEstimate'] = adjustEstimate
        if newEstimate is not None:
            _query['newEstimate'] = newEstimate
        if expand is not None:
            _query['expand'] = expand
        if overrideEditableFlag is not None:
            _query['overrideEditableFlag'] = overrideEditableFlag
        _body: Dict[str, Any] = {}
        if author is not None:
            _body['author'] = author
        if comment is not None:
            _body['comment'] = comment
        if created is not None:
            _body['created'] = created
        if id_body is not None:
            _body['id'] = id_body
        if issueId is not None:
            _body['issueId'] = issueId
        if properties is not None:
            _body['properties'] = properties
        if self_ is not None:
            _body['self'] = self_
        if started is not None:
            _body['started'] = started
        if timeSpent is not None:
            _body['timeSpent'] = timeSpent
        if timeSpentSeconds is not None:
            _body['timeSpentSeconds'] = timeSpentSeconds
        if updateAuthor is not None:
            _body['updateAuthor'] = updateAuthor
        if updated is not None:
            _body['updated'] = updated
        if visibility is not None:
            _body['visibility'] = visibility
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_worklog_property_keys(self, issueIdOrKey: str, worklogId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get worklog property keys

HTTP GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties
Path params:
  - issueIdOrKey (str)
  - worklogId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'worklogId': worklogId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_worklog_property(self, issueIdOrKey: str, worklogId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete worklog property

HTTP DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}
Path params:
  - issueIdOrKey (str)
  - worklogId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'worklogId': worklogId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_worklog_property(self, issueIdOrKey: str, worklogId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get worklog property

HTTP GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}
Path params:
  - issueIdOrKey (str)
  - worklogId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'worklogId': worklogId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_worklog_property(self, issueIdOrKey: str, worklogId: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set worklog property

HTTP PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}
Path params:
  - issueIdOrKey (str)
  - worklogId (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueIdOrKey': issueIdOrKey, 'worklogId': worklogId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def link_issues(self, inwardIssue: Dict[str, Any], outwardIssue: Dict[str, Any], type: Dict[str, Any], comment: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue link

HTTP POST /rest/api/3/issueLink
Body (application/json) fields:
  - comment (Dict[str, Any], optional)
  - inwardIssue (Dict[str, Any], required)
  - outwardIssue (Dict[str, Any], required)
  - type (Dict[str, Any], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if comment is not None:
            _body['comment'] = comment
        _body['inwardIssue'] = inwardIssue
        _body['outwardIssue'] = outwardIssue
        _body['type'] = type
        rel_path = '/rest/api/3/issueLink'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue_link(self, linkId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue link

HTTP DELETE /rest/api/3/issueLink/{linkId}
Path params:
  - linkId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'linkId': linkId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issueLink/{linkId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_link(self, linkId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue link

HTTP GET /rest/api/3/issueLink/{linkId}
Path params:
  - linkId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'linkId': linkId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issueLink/{linkId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_link_types(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue link types

HTTP GET /rest/api/3/issueLinkType"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issueLinkType'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_link_type(self, id: Optional[str]=None, inward: Optional[str]=None, name: Optional[str]=None, outward: Optional[str]=None, self_: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue link type

HTTP POST /rest/api/3/issueLinkType
Body (application/json) fields:
  - id (str, optional)
  - inward (str, optional)
  - name (str, optional)
  - outward (str, optional)
  - self (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if id is not None:
            _body['id'] = id
        if inward is not None:
            _body['inward'] = inward
        if name is not None:
            _body['name'] = name
        if outward is not None:
            _body['outward'] = outward
        if self_ is not None:
            _body['self'] = self_
        rel_path = '/rest/api/3/issueLinkType'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue_link_type(self, issueLinkTypeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue link type

HTTP DELETE /rest/api/3/issueLinkType/{issueLinkTypeId}
Path params:
  - issueLinkTypeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueLinkTypeId': issueLinkTypeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issueLinkType/{issueLinkTypeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_link_type(self, issueLinkTypeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue link type

HTTP GET /rest/api/3/issueLinkType/{issueLinkTypeId}
Path params:
  - issueLinkTypeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueLinkTypeId': issueLinkTypeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issueLinkType/{issueLinkTypeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_issue_link_type(self, issueLinkTypeId: str, id: Optional[str]=None, inward: Optional[str]=None, name: Optional[str]=None, outward: Optional[str]=None, self_: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue link type

HTTP PUT /rest/api/3/issueLinkType/{issueLinkTypeId}
Path params:
  - issueLinkTypeId (str)
Body (application/json) fields:
  - id (str, optional)
  - inward (str, optional)
  - name (str, optional)
  - outward (str, optional)
  - self (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueLinkTypeId': issueLinkTypeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if id is not None:
            _body['id'] = id
        if inward is not None:
            _body['inward'] = inward
        if name is not None:
            _body['name'] = name
        if outward is not None:
            _body['outward'] = outward
        if self_ is not None:
            _body['self'] = self_
        rel_path = '/rest/api/3/issueLinkType/{issueLinkTypeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def export_archived_issues(self, archivedBy: Optional[list[str]]=None, archivedDateRange: Optional[Dict[str, Any]]=None, issueTypes: Optional[list[str]]=None, projects: Optional[list[str]]=None, reporters: Optional[list[str]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Export archived issue(s)

HTTP PUT /rest/api/3/issues/archive/export
Body (application/json) fields:
  - archivedBy (list[str], optional)
  - archivedDateRange (Dict[str, Any], optional)
  - issueTypes (list[str], optional)
  - projects (list[str], optional)
  - reporters (list[str], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if archivedBy is not None:
            _body['archivedBy'] = archivedBy
        if archivedDateRange is not None:
            _body['archivedDateRange'] = archivedDateRange
        if issueTypes is not None:
            _body['issueTypes'] = issueTypes
        if projects is not None:
            _body['projects'] = projects
        if reporters is not None:
            _body['reporters'] = reporters
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issues/archive/export'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_security_schemes(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue security schemes

HTTP GET /rest/api/3/issuesecurityschemes"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_security_scheme(self, name: str, description: Optional[str]=None, levels: Optional[list[Dict[str, Any]]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue security scheme

HTTP POST /rest/api/3/issuesecurityschemes
Body (application/json) fields:
  - description (str, optional)
  - levels (list[Dict[str, Any]], optional)
  - name (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if levels is not None:
            _body['levels'] = levels
        _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issuesecurityschemes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_security_levels(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, id: Optional[list[str]]=None, schemeId: Optional[list[str]]=None, onlyDefault: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue security levels

HTTP GET /rest/api/3/issuesecurityschemes/level
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - id (list[str], optional)
  - schemeId (list[str], optional)
  - onlyDefault (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if schemeId is not None:
            _query['schemeId'] = schemeId
        if onlyDefault is not None:
            _query['onlyDefault'] = onlyDefault
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/level'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_default_levels(self, defaultValues: list[Dict[str, Any]], body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set default issue security levels

HTTP PUT /rest/api/3/issuesecurityschemes/level/default
Body (application/json) fields:
  - defaultValues (list[Dict[str, Any]], required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['defaultValues'] = defaultValues
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issuesecurityschemes/level/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_security_level_members(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, id: Optional[list[str]]=None, schemeId: Optional[list[str]]=None, levelId: Optional[list[str]]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue security level members

HTTP GET /rest/api/3/issuesecurityschemes/level/member
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - id (list[str], optional)
  - schemeId (list[str], optional)
  - levelId (list[str], optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if schemeId is not None:
            _query['schemeId'] = schemeId
        if levelId is not None:
            _query['levelId'] = levelId
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/level/member'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_projects_using_security_schemes(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, issueSecuritySchemeId: Optional[list[str]]=None, projectId: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get projects using issue security schemes

HTTP GET /rest/api/3/issuesecurityschemes/project
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - issueSecuritySchemeId (list[str], optional)
  - projectId (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if issueSecuritySchemeId is not None:
            _query['issueSecuritySchemeId'] = issueSecuritySchemeId
        if projectId is not None:
            _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def associate_schemes_to_projects(self, projectId: str, schemeId: str, oldToNewSecurityLevelMappings: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Associate security scheme to project

HTTP PUT /rest/api/3/issuesecurityschemes/project
Body (application/json) fields:
  - oldToNewSecurityLevelMappings (list[Dict[str, Any]], optional)
  - projectId (str, required)
  - schemeId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if oldToNewSecurityLevelMappings is not None:
            _body['oldToNewSecurityLevelMappings'] = oldToNewSecurityLevelMappings
        _body['projectId'] = projectId
        _body['schemeId'] = schemeId
        rel_path = '/rest/api/3/issuesecurityschemes/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_security_schemes(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, id: Optional[list[str]]=None, projectId: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search issue security schemes

HTTP GET /rest/api/3/issuesecurityschemes/search
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - id (list[str], optional)
  - projectId (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if projectId is not None:
            _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_security_scheme(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue security scheme

HTTP GET /rest/api/3/issuesecurityschemes/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_issue_security_scheme(self, id: str, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue security scheme

HTTP PUT /rest/api/3/issuesecurityschemes/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/issuesecurityschemes/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_security_level_members(self, issueSecuritySchemeId: int, startAt: Optional[int]=None, maxResults: Optional[int]=None, issueSecurityLevelId: Optional[list[str]]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue security level members by issue security scheme

HTTP GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members
Path params:
  - issueSecuritySchemeId (int)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - issueSecurityLevelId (list[str], optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueSecuritySchemeId': issueSecuritySchemeId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if issueSecurityLevelId is not None:
            _query['issueSecurityLevelId'] = issueSecurityLevelId
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_security_scheme(self, schemeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue security scheme

HTTP DELETE /rest/api/3/issuesecurityschemes/{schemeId}
Path params:
  - schemeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/{schemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_security_level(self, schemeId: str, levels: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add issue security levels

HTTP PUT /rest/api/3/issuesecurityschemes/{schemeId}/level
Path params:
  - schemeId (str)
Body (application/json) fields:
  - levels (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if levels is not None:
            _body['levels'] = levels
        rel_path = '/rest/api/3/issuesecurityschemes/{schemeId}/level'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_level(self, schemeId: str, levelId: str, replaceWith: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove issue security level

HTTP DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}
Path params:
  - schemeId (str)
  - levelId (str)
Query params:
  - replaceWith (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId, 'levelId': levelId}
        _query: Dict[str, Any] = {}
        if replaceWith is not None:
            _query['replaceWith'] = replaceWith
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_security_level(self, schemeId: str, levelId: str, description: Optional[str]=None, name: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue security level

HTTP PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}
Path params:
  - schemeId (str)
  - levelId (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'schemeId': schemeId, 'levelId': levelId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_security_level_members(self, schemeId: str, levelId: str, members: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add issue security level members

HTTP PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member
Path params:
  - schemeId (str)
  - levelId (str)
Body (application/json) fields:
  - members (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'schemeId': schemeId, 'levelId': levelId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if members is not None:
            _body['members'] = members
        rel_path = '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_member_from_security_level(self, schemeId: str, levelId: str, memberId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove member from issue security level

HTTP DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}
Path params:
  - schemeId (str)
  - levelId (str)
  - memberId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId, 'levelId': levelId, 'memberId': memberId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_all_types(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all issue types for user

HTTP GET /rest/api/3/issuetype"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetype'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_type(self, name: str, description: Optional[str]=None, hierarchyLevel: Optional[int]=None, type: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue type

HTTP POST /rest/api/3/issuetype
Body (application/json) fields:
  - description (str, optional)
  - hierarchyLevel (int, optional)
  - name (str, required)
  - type (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if hierarchyLevel is not None:
            _body['hierarchyLevel'] = hierarchyLevel
        _body['name'] = name
        if type is not None:
            _body['type'] = type
        rel_path = '/rest/api/3/issuetype'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_types_for_project(self, projectId: int, level: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue types for project

HTTP GET /rest/api/3/issuetype/project
Query params:
  - projectId (int, required)
  - level (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['projectId'] = projectId
        if level is not None:
            _query['level'] = level
        _body = None
        rel_path = '/rest/api/3/issuetype/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue_type(self, id: str, alternativeIssueTypeId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue type

HTTP DELETE /rest/api/3/issuetype/{id}
Path params:
  - id (str)
Query params:
  - alternativeIssueTypeId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if alternativeIssueTypeId is not None:
            _query['alternativeIssueTypeId'] = alternativeIssueTypeId
        _body = None
        rel_path = '/rest/api/3/issuetype/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type

HTTP GET /rest/api/3/issuetype/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetype/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_issue_type(self, id: str, avatarId: Optional[int]=None, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue type

HTTP PUT /rest/api/3/issuetype/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - avatarId (int, optional)
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if avatarId is not None:
            _body['avatarId'] = avatarId
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/issuetype/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_alternative_issue_types(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get alternative issue types

HTTP GET /rest/api/3/issuetype/{id}/alternatives
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetype/{id}/alternatives'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_type_avatar(self, id: str, size: int, x: Optional[int]=None, y: Optional[int]=None, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Load issue type avatar

HTTP POST /rest/api/3/issuetype/{id}/avatar2
Path params:
  - id (str)
Query params:
  - x (int, optional)
  - y (int, optional)
  - size (int, required)
Body: */* (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', '*/*')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if x is not None:
            _query['x'] = x
        if y is not None:
            _query['y'] = y
        _query['size'] = size
        _body = body
        rel_path = '/rest/api/3/issuetype/{id}/avatar2'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_property_keys(self, issueTypeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type property keys

HTTP GET /rest/api/3/issuetype/{issueTypeId}/properties
Path params:
  - issueTypeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueTypeId': issueTypeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetype/{issueTypeId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue_type_property(self, issueTypeId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue type property

HTTP DELETE /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}
Path params:
  - issueTypeId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueTypeId': issueTypeId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_property(self, issueTypeId: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type property

HTTP GET /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}
Path params:
  - issueTypeId (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueTypeId': issueTypeId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_issue_type_property(self, issueTypeId: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set issue type property

HTTP PUT /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}
Path params:
  - issueTypeId (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeId': issueTypeId, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_issue_type_schemes(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[int]]=None, orderBy: Optional[str]=None, expand: Optional[str]=None, queryString: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all issue type schemes

HTTP GET /rest/api/3/issuetypescheme
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[int], optional)
  - orderBy (str, optional)
  - expand (str, optional)
  - queryString (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if expand is not None:
            _query['expand'] = expand
        if queryString is not None:
            _query['queryString'] = queryString
        _body = None
        rel_path = '/rest/api/3/issuetypescheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_type_scheme(self, issueTypeIds: list[str], name: str, defaultIssueTypeId: Optional[str]=None, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue type scheme

HTTP POST /rest/api/3/issuetypescheme
Body (application/json) fields:
  - defaultIssueTypeId (str, optional)
  - description (str, optional)
  - issueTypeIds (list[str], required)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultIssueTypeId is not None:
            _body['defaultIssueTypeId'] = defaultIssueTypeId
        if description is not None:
            _body['description'] = description
        _body['issueTypeIds'] = issueTypeIds
        _body['name'] = name
        rel_path = '/rest/api/3/issuetypescheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_schemes_mapping(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, issueTypeSchemeId: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type scheme items

HTTP GET /rest/api/3/issuetypescheme/mapping
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - issueTypeSchemeId (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if issueTypeSchemeId is not None:
            _query['issueTypeSchemeId'] = issueTypeSchemeId
        _body = None
        rel_path = '/rest/api/3/issuetypescheme/mapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_scheme_for_projects(self, projectId: list[int], startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type schemes for projects

HTTP GET /rest/api/3/issuetypescheme/project
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - projectId (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/issuetypescheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_issue_type_scheme_to_project(self, issueTypeSchemeId: str, projectId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign issue type scheme to project

HTTP PUT /rest/api/3/issuetypescheme/project
Body (application/json) fields:
  - issueTypeSchemeId (str, required)
  - projectId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeSchemeId'] = issueTypeSchemeId
        _body['projectId'] = projectId
        rel_path = '/rest/api/3/issuetypescheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_issue_type_scheme(self, issueTypeSchemeId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue type scheme

HTTP DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}
Path params:
  - issueTypeSchemeId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueTypeSchemeId': issueTypeSchemeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetypescheme/{issueTypeSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_issue_type_scheme(self, issueTypeSchemeId: int, defaultIssueTypeId: Optional[str]=None, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue type scheme

HTTP PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}
Path params:
  - issueTypeSchemeId (int)
Body (application/json) fields:
  - defaultIssueTypeId (str, optional)
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeSchemeId': issueTypeSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultIssueTypeId is not None:
            _body['defaultIssueTypeId'] = defaultIssueTypeId
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/issuetypescheme/{issueTypeSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_issue_types_to_issue_type_scheme(self, issueTypeSchemeId: int, issueTypeIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add issue types to issue type scheme

HTTP PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype
Path params:
  - issueTypeSchemeId (int)
Body (application/json) fields:
  - issueTypeIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeSchemeId': issueTypeSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeIds'] = issueTypeIds
        rel_path = '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def reorder_issue_types_in_issue_type_scheme(self, issueTypeSchemeId: int, issueTypeIds: list[str], after: Optional[str]=None, position: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Change order of issue types

HTTP PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move
Path params:
  - issueTypeSchemeId (int)
Body (application/json) fields:
  - after (str, optional)
  - issueTypeIds (list[str], required)
  - position (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeSchemeId': issueTypeSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if after is not None:
            _body['after'] = after
        _body['issueTypeIds'] = issueTypeIds
        if position is not None:
            _body['position'] = position
        rel_path = '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_issue_type_from_issue_type_scheme(self, issueTypeSchemeId: int, issueTypeId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove issue type from issue type scheme

HTTP DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}
Path params:
  - issueTypeSchemeId (int)
  - issueTypeId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueTypeSchemeId': issueTypeSchemeId, 'issueTypeId': issueTypeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_screen_schemes(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[int]]=None, queryString: Optional[str]=None, orderBy: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type screen schemes

HTTP GET /rest/api/3/issuetypescreenscheme
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[int], optional)
  - queryString (str, optional)
  - orderBy (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if queryString is not None:
            _query['queryString'] = queryString
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/issuetypescreenscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_issue_type_screen_scheme(self, issueTypeMappings: list[Dict[str, Any]], name: str, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create issue type screen scheme

HTTP POST /rest/api/3/issuetypescreenscheme
Body (application/json) fields:
  - description (str, optional)
  - issueTypeMappings (list[Dict[str, Any]], required)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['issueTypeMappings'] = issueTypeMappings
        _body['name'] = name
        rel_path = '/rest/api/3/issuetypescreenscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_screen_scheme_mappings(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, issueTypeScreenSchemeId: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type screen scheme items

HTTP GET /rest/api/3/issuetypescreenscheme/mapping
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - issueTypeScreenSchemeId (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if issueTypeScreenSchemeId is not None:
            _query['issueTypeScreenSchemeId'] = issueTypeScreenSchemeId
        _body = None
        rel_path = '/rest/api/3/issuetypescreenscheme/mapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_type_screen_scheme_project_associations(self, projectId: list[int], startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type screen schemes for projects

HTTP GET /rest/api/3/issuetypescreenscheme/project
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - projectId (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/issuetypescreenscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_issue_type_screen_scheme_to_project(self, issueTypeScreenSchemeId: Optional[str]=None, projectId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign issue type screen scheme to project

HTTP PUT /rest/api/3/issuetypescreenscheme/project
Body (application/json) fields:
  - issueTypeScreenSchemeId (str, optional)
  - projectId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issueTypeScreenSchemeId is not None:
            _body['issueTypeScreenSchemeId'] = issueTypeScreenSchemeId
        if projectId is not None:
            _body['projectId'] = projectId
        rel_path = '/rest/api/3/issuetypescreenscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    @codeflash_behavior_async
    async def delete_issue_type_screen_scheme(self, issueTypeScreenSchemeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue type screen scheme

HTTP DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}
Path params:
  - issueTypeScreenSchemeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers = headers if headers is not None else {}
        _path = {'issueTypeScreenSchemeId': issueTypeScreenSchemeId}
        rel_path = '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params={}, body=None)
        resp = await self._client.execute(req)
        return resp

    async def update_issue_type_screen_scheme(self, issueTypeScreenSchemeId: str, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue type screen scheme

HTTP PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}
Path params:
  - issueTypeScreenSchemeId (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeScreenSchemeId': issueTypeScreenSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def append_mappings_for_issue_type_screen_scheme(self, issueTypeScreenSchemeId: str, issueTypeMappings: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Append mappings to issue type screen scheme

HTTP PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping
Path params:
  - issueTypeScreenSchemeId (str)
Body (application/json) fields:
  - issueTypeMappings (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeScreenSchemeId': issueTypeScreenSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeMappings'] = issueTypeMappings
        rel_path = '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_default_screen_scheme(self, issueTypeScreenSchemeId: str, screenSchemeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update issue type screen scheme default screen scheme

HTTP PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default
Path params:
  - issueTypeScreenSchemeId (str)
Body (application/json) fields:
  - screenSchemeId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeScreenSchemeId': issueTypeScreenSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['screenSchemeId'] = screenSchemeId
        rel_path = '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_mappings_from_issue_type_screen_scheme(self, issueTypeScreenSchemeId: str, issueTypeIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove mappings from issue type screen scheme

HTTP POST /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove
Path params:
  - issueTypeScreenSchemeId (str)
Body (application/json) fields:
  - issueTypeIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'issueTypeScreenSchemeId': issueTypeScreenSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueTypeIds'] = issueTypeIds
        rel_path = '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_projects_for_issue_type_screen_scheme(self, issueTypeScreenSchemeId: int, startAt: Optional[int]=None, maxResults: Optional[int]=None, query: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type screen scheme projects

HTTP GET /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project
Path params:
  - issueTypeScreenSchemeId (int)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - query (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'issueTypeScreenSchemeId': issueTypeScreenSchemeId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if query is not None:
            _query['query'] = query
        _body = None
        rel_path = '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_auto_complete(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get field reference data (GET)

HTTP GET /rest/api/3/jql/autocompletedata"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/jql/autocompletedata'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_auto_complete_post(self, includeCollapsedFields: Optional[bool]=None, projectIds: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get field reference data (POST)

HTTP POST /rest/api/3/jql/autocompletedata
Body (application/json) fields:
  - includeCollapsedFields (bool, optional)
  - projectIds (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if includeCollapsedFields is not None:
            _body['includeCollapsedFields'] = includeCollapsedFields
        if projectIds is not None:
            _body['projectIds'] = projectIds
        rel_path = '/rest/api/3/jql/autocompletedata'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_field_auto_complete_for_query_string(self, fieldName: Optional[str]=None, fieldValue: Optional[str]=None, predicateName: Optional[str]=None, predicateValue: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get field auto complete suggestions

HTTP GET /rest/api/3/jql/autocompletedata/suggestions
Query params:
  - fieldName (str, optional)
  - fieldValue (str, optional)
  - predicateName (str, optional)
  - predicateValue (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if fieldName is not None:
            _query['fieldName'] = fieldName
        if fieldValue is not None:
            _query['fieldValue'] = fieldValue
        if predicateName is not None:
            _query['predicateName'] = predicateName
        if predicateValue is not None:
            _query['predicateValue'] = predicateValue
        _body = None
        rel_path = '/rest/api/3/jql/autocompletedata/suggestions'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_precomputations(self, functionKey: Optional[list[str]]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, orderBy: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get precomputations (apps)

HTTP GET /rest/api/3/jql/function/computation
Query params:
  - functionKey (list[str], optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - orderBy (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if functionKey is not None:
            _query['functionKey'] = functionKey
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if orderBy is not None:
            _query['orderBy'] = orderBy
        _body = None
        rel_path = '/rest/api/3/jql/function/computation'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_precomputations(self, skipNotFoundPrecomputations: Optional[bool]=None, values: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update precomputations (apps)

HTTP POST /rest/api/3/jql/function/computation
Query params:
  - skipNotFoundPrecomputations (bool, optional)
Body (application/json) fields:
  - values (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if skipNotFoundPrecomputations is not None:
            _query['skipNotFoundPrecomputations'] = skipNotFoundPrecomputations
        _body: Dict[str, Any] = {}
        if values is not None:
            _body['values'] = values
        rel_path = '/rest/api/3/jql/function/computation'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_precomputations_by_id(self, orderBy: Optional[str]=None, precomputationIDs: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get precomputations by ID (apps)

HTTP POST /rest/api/3/jql/function/computation/search
Query params:
  - orderBy (str, optional)
Body (application/json) fields:
  - precomputationIDs (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if orderBy is not None:
            _query['orderBy'] = orderBy
        _body: Dict[str, Any] = {}
        if precomputationIDs is not None:
            _body['precomputationIDs'] = precomputationIDs
        rel_path = '/rest/api/3/jql/function/computation/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def match_issues(self, issueIds: list[int], jqls: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Check issues against JQL

HTTP POST /rest/api/3/jql/match
Body (application/json) fields:
  - issueIds (list[int], required)
  - jqls (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['issueIds'] = issueIds
        _body['jqls'] = jqls
        rel_path = '/rest/api/3/jql/match'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def parse_jql_queries(self, validation: str, queries: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Parse JQL query

HTTP POST /rest/api/3/jql/parse
Query params:
  - validation (str, required)
Body (application/json) fields:
  - queries (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['validation'] = validation
        _body: Dict[str, Any] = {}
        _body['queries'] = queries
        rel_path = '/rest/api/3/jql/parse'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def migrate_queries(self, queryStrings: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Convert user identifiers to account IDs in JQL queries

HTTP POST /rest/api/3/jql/pdcleaner
Body (application/json) fields:
  - queryStrings (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if queryStrings is not None:
            _body['queryStrings'] = queryStrings
        rel_path = '/rest/api/3/jql/pdcleaner'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def sanitise_jql_queries(self, queries: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Sanitize JQL queries

HTTP POST /rest/api/3/jql/sanitize
Body (application/json) fields:
  - queries (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['queries'] = queries
        rel_path = '/rest/api/3/jql/sanitize'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_labels(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all labels

HTTP GET /rest/api/3/label
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/label'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_approximate_license_count(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get approximate license count

HTTP GET /rest/api/3/license/approximateLicenseCount"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/license/approximateLicenseCount'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_approximate_application_license_count(self, applicationKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get approximate application license count

HTTP GET /rest/api/3/license/approximateLicenseCount/product/{applicationKey}
Path params:
  - applicationKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'applicationKey': applicationKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/license/approximateLicenseCount/product/{applicationKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_my_permissions(self, projectKey: Optional[str]=None, projectId: Optional[str]=None, issueKey: Optional[str]=None, issueId: Optional[str]=None, permissions: Optional[str]=None, projectUuid: Optional[str]=None, projectConfigurationUuid: Optional[str]=None, commentId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get my permissions

HTTP GET /rest/api/3/mypermissions
Query params:
  - projectKey (str, optional)
  - projectId (str, optional)
  - issueKey (str, optional)
  - issueId (str, optional)
  - permissions (str, optional)
  - projectUuid (str, optional)
  - projectConfigurationUuid (str, optional)
  - commentId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if projectKey is not None:
            _query['projectKey'] = projectKey
        if projectId is not None:
            _query['projectId'] = projectId
        if issueKey is not None:
            _query['issueKey'] = issueKey
        if issueId is not None:
            _query['issueId'] = issueId
        if permissions is not None:
            _query['permissions'] = permissions
        if projectUuid is not None:
            _query['projectUuid'] = projectUuid
        if projectConfigurationUuid is not None:
            _query['projectConfigurationUuid'] = projectConfigurationUuid
        if commentId is not None:
            _query['commentId'] = commentId
        _body = None
        rel_path = '/rest/api/3/mypermissions'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_preference(self, key: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete preference

HTTP DELETE /rest/api/3/mypreferences
Query params:
  - key (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/mypreferences'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_preference(self, key: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get preference

HTTP GET /rest/api/3/mypreferences
Query params:
  - key (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/mypreferences'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_preference(self, key: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set preference

HTTP PUT /rest/api/3/mypreferences
Query params:
  - key (str, required)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['key'] = key
        _body = body
        rel_path = '/rest/api/3/mypreferences'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_locale(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get locale

HTTP GET /rest/api/3/mypreferences/locale"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/mypreferences/locale'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_locale(self, locale: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set locale

HTTP PUT /rest/api/3/mypreferences/locale
Body (application/json) fields:
  - locale (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if locale is not None:
            _body['locale'] = locale
        rel_path = '/rest/api/3/mypreferences/locale'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    @codeflash_performance_async
    async def get_current_user(self, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get current user

HTTP GET /rest/api/3/myself
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = headers if headers is not None else {}
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {'expand': expand} if expand is not None else {}
        _body = None
        rel_path = '/rest/api/3/myself'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_notification_schemes(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, id: Optional[list[str]]=None, projectId: Optional[list[str]]=None, onlyDefault: Optional[bool]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get notification schemes paginated

HTTP GET /rest/api/3/notificationscheme
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - id (list[str], optional)
  - projectId (list[str], optional)
  - onlyDefault (bool, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if projectId is not None:
            _query['projectId'] = projectId
        if onlyDefault is not None:
            _query['onlyDefault'] = onlyDefault
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/notificationscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_notification_scheme(self, name: str, description: Optional[str]=None, notificationSchemeEvents: Optional[list[Dict[str, Any]]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create notification scheme

HTTP POST /rest/api/3/notificationscheme
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)
  - notificationSchemeEvents (list[Dict[str, Any]], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        if notificationSchemeEvents is not None:
            _body['notificationSchemeEvents'] = notificationSchemeEvents
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/notificationscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_notification_scheme_to_project_mappings(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, notificationSchemeId: Optional[list[str]]=None, projectId: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get projects using notification schemes paginated

HTTP GET /rest/api/3/notificationscheme/project
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - notificationSchemeId (list[str], optional)
  - projectId (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if notificationSchemeId is not None:
            _query['notificationSchemeId'] = notificationSchemeId
        if projectId is not None:
            _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/notificationscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_notification_scheme(self, id: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get notification scheme

HTTP GET /rest/api/3/notificationscheme/{id}
Path params:
  - id (int)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/notificationscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_notification_scheme(self, id: str, description: Optional[str]=None, name: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update notification scheme

HTTP PUT /rest/api/3/notificationscheme/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/notificationscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_notifications(self, id: str, notificationSchemeEvents: list[Dict[str, Any]], body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add notifications to notification scheme

HTTP PUT /rest/api/3/notificationscheme/{id}/notification
Path params:
  - id (str)
Body (application/json) fields:
  - notificationSchemeEvents (list[Dict[str, Any]], required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['notificationSchemeEvents'] = notificationSchemeEvents
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/notificationscheme/{id}/notification'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_notification_scheme(self, notificationSchemeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete notification scheme

HTTP DELETE /rest/api/3/notificationscheme/{notificationSchemeId}
Path params:
  - notificationSchemeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'notificationSchemeId': notificationSchemeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/notificationscheme/{notificationSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_notification_from_notification_scheme(self, notificationSchemeId: str, notificationId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove notification from notification scheme

HTTP DELETE /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}
Path params:
  - notificationSchemeId (str)
  - notificationId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'notificationSchemeId': notificationSchemeId, 'notificationId': notificationId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_permissions(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all permissions

HTTP GET /rest/api/3/permissions"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/permissions'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_bulk_permissions(self, accountId: Optional[str]=None, globalPermissions: Optional[list[str]]=None, projectPermissions: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get bulk permissions

HTTP POST /rest/api/3/permissions/check
Body (application/json) fields:
  - accountId (str, optional)
  - globalPermissions (list[str], optional)
  - projectPermissions (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if accountId is not None:
            _body['accountId'] = accountId
        if globalPermissions is not None:
            _body['globalPermissions'] = globalPermissions
        if projectPermissions is not None:
            _body['projectPermissions'] = projectPermissions
        rel_path = '/rest/api/3/permissions/check'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_permitted_projects(self, permissions: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get permitted projects

HTTP POST /rest/api/3/permissions/project
Body (application/json) fields:
  - permissions (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['permissions'] = permissions
        rel_path = '/rest/api/3/permissions/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_permission_schemes(self, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all permission schemes

HTTP GET /rest/api/3/permissionscheme
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/permissionscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_permission_scheme(self, name: str, expand: Optional[str]=None, description: Optional[str]=None, expand_body: Optional[str]=None, id: Optional[int]=None, permissions: Optional[list[Dict[str, Any]]]=None, scope: Optional[Dict[str, Any]]=None, self_: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create permission scheme

HTTP POST /rest/api/3/permissionscheme
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - description (str, optional)
  - expand (str, optional)
  - id (int, optional)
  - name (str, required)
  - permissions (list[Dict[str, Any]], optional)
  - scope (Dict[str, Any], optional)
  - self (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if expand_body is not None:
            _body['expand'] = expand_body
        if id is not None:
            _body['id'] = id
        _body['name'] = name
        if permissions is not None:
            _body['permissions'] = permissions
        if scope is not None:
            _body['scope'] = scope
        if self_ is not None:
            _body['self'] = self_
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/permissionscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_permission_scheme(self, schemeId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete permission scheme

HTTP DELETE /rest/api/3/permissionscheme/{schemeId}
Path params:
  - schemeId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/permissionscheme/{schemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_permission_scheme(self, schemeId: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get permission scheme

HTTP GET /rest/api/3/permissionscheme/{schemeId}
Path params:
  - schemeId (int)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/permissionscheme/{schemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_permission_scheme(self, schemeId: int, name: str, expand: Optional[str]=None, description: Optional[str]=None, expand_body: Optional[str]=None, id: Optional[int]=None, permissions: Optional[list[Dict[str, Any]]]=None, scope: Optional[Dict[str, Any]]=None, self_: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update permission scheme

HTTP PUT /rest/api/3/permissionscheme/{schemeId}
Path params:
  - schemeId (int)
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - description (str, optional)
  - expand (str, optional)
  - id (int, optional)
  - name (str, required)
  - permissions (list[Dict[str, Any]], optional)
  - scope (Dict[str, Any], optional)
  - self (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if expand_body is not None:
            _body['expand'] = expand_body
        if id is not None:
            _body['id'] = id
        _body['name'] = name
        if permissions is not None:
            _body['permissions'] = permissions
        if scope is not None:
            _body['scope'] = scope
        if self_ is not None:
            _body['self'] = self_
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/permissionscheme/{schemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_permission_scheme_grants(self, schemeId: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get permission scheme grants

HTTP GET /rest/api/3/permissionscheme/{schemeId}/permission
Path params:
  - schemeId (int)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/permissionscheme/{schemeId}/permission'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_permission_grant(self, schemeId: int, expand: Optional[str]=None, holder: Optional[Dict[str, Any]]=None, id: Optional[int]=None, permission: Optional[str]=None, self_: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create permission grant

HTTP POST /rest/api/3/permissionscheme/{schemeId}/permission
Path params:
  - schemeId (int)
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - holder (Dict[str, Any], optional)
  - id (int, optional)
  - permission (str, optional)
  - self (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if holder is not None:
            _body['holder'] = holder
        if id is not None:
            _body['id'] = id
        if permission is not None:
            _body['permission'] = permission
        if self_ is not None:
            _body['self'] = self_
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/permissionscheme/{schemeId}/permission'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_permission_scheme_entity(self, schemeId: int, permissionId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete permission scheme grant

HTTP DELETE /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}
Path params:
  - schemeId (int)
  - permissionId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId, 'permissionId': permissionId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_permission_scheme_grant(self, schemeId: int, permissionId: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get permission scheme grant

HTTP GET /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}
Path params:
  - schemeId (int)
  - permissionId (int)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId, 'permissionId': permissionId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_plans(self, includeTrashed: Optional[bool]=None, includeArchived: Optional[bool]=None, cursor: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get plans paginated

HTTP GET /rest/api/3/plans/plan
Query params:
  - includeTrashed (bool, optional)
  - includeArchived (bool, optional)
  - cursor (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if includeTrashed is not None:
            _query['includeTrashed'] = includeTrashed
        if includeArchived is not None:
            _query['includeArchived'] = includeArchived
        if cursor is not None:
            _query['cursor'] = cursor
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/plans/plan'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_plan(self, issueSources: list[Dict[str, Any]], name: str, scheduling: Dict[str, Any], useGroupId: Optional[bool]=None, crossProjectReleases: Optional[list[Dict[str, Any]]]=None, customFields: Optional[list[Dict[str, Any]]]=None, exclusionRules: Optional[Dict[str, Any]]=None, leadAccountId: Optional[str]=None, permissions: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create plan

HTTP POST /rest/api/3/plans/plan
Query params:
  - useGroupId (bool, optional)
Body (application/json) fields:
  - crossProjectReleases (list[Dict[str, Any]], optional)
  - customFields (list[Dict[str, Any]], optional)
  - exclusionRules (Dict[str, Any], optional)
  - issueSources (list[Dict[str, Any]], required)
  - leadAccountId (str, optional)
  - name (str, required)
  - permissions (list[Dict[str, Any]], optional)
  - scheduling (Dict[str, Any], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if useGroupId is not None:
            _query['useGroupId'] = useGroupId
        _body: Dict[str, Any] = {}
        if crossProjectReleases is not None:
            _body['crossProjectReleases'] = crossProjectReleases
        if customFields is not None:
            _body['customFields'] = customFields
        if exclusionRules is not None:
            _body['exclusionRules'] = exclusionRules
        _body['issueSources'] = issueSources
        if leadAccountId is not None:
            _body['leadAccountId'] = leadAccountId
        _body['name'] = name
        if permissions is not None:
            _body['permissions'] = permissions
        _body['scheduling'] = scheduling
        rel_path = '/rest/api/3/plans/plan'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_plan(self, planId: int, useGroupId: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get plan

HTTP GET /rest/api/3/plans/plan/{planId}
Path params:
  - planId (int)
Query params:
  - useGroupId (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        if useGroupId is not None:
            _query['useGroupId'] = useGroupId
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_plan(self, planId: int, useGroupId: Optional[bool]=None, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update plan

HTTP PUT /rest/api/3/plans/plan/{planId}
Path params:
  - planId (int)
Query params:
  - useGroupId (bool, optional)
Body: application/json-patch+json (Dict[str, Any])"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json-patch+json')
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        if useGroupId is not None:
            _query['useGroupId'] = useGroupId
        _body = body
        rel_path = '/rest/api/3/plans/plan/{planId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def archive_plan(self, planId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Archive plan

HTTP PUT /rest/api/3/plans/plan/{planId}/archive
Path params:
  - planId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/archive'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def duplicate_plan(self, planId: int, name: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Duplicate plan

HTTP POST /rest/api/3/plans/plan/{planId}/duplicate
Path params:
  - planId (int)
Body (application/json) fields:
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['name'] = name
        rel_path = '/rest/api/3/plans/plan/{planId}/duplicate'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_teams(self, planId: int, cursor: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get teams in plan paginated

HTTP GET /rest/api/3/plans/plan/{planId}/team
Path params:
  - planId (int)
Query params:
  - cursor (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        if cursor is not None:
            _query['cursor'] = cursor
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/team'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_atlassian_team(self, planId: int, id: str, planningStyle: str, capacity: Optional[float]=None, issueSourceId: Optional[int]=None, sprintLength: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add Atlassian team to plan

HTTP POST /rest/api/3/plans/plan/{planId}/team/atlassian
Path params:
  - planId (int)
Body (application/json) fields:
  - capacity (float, optional)
  - id (str, required)
  - issueSourceId (int, optional)
  - planningStyle (str, required)
  - sprintLength (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if capacity is not None:
            _body['capacity'] = capacity
        _body['id'] = id
        if issueSourceId is not None:
            _body['issueSourceId'] = issueSourceId
        _body['planningStyle'] = planningStyle
        if sprintLength is not None:
            _body['sprintLength'] = sprintLength
        rel_path = '/rest/api/3/plans/plan/{planId}/team/atlassian'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_atlassian_team(self, planId: int, atlassianTeamId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove Atlassian team from plan

HTTP DELETE /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}
Path params:
  - planId (int)
  - atlassianTeamId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId, 'atlassianTeamId': atlassianTeamId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_atlassian_team(self, planId: int, atlassianTeamId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get Atlassian team in plan

HTTP GET /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}
Path params:
  - planId (int)
  - atlassianTeamId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId, 'atlassianTeamId': atlassianTeamId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_atlassian_team(self, planId: int, atlassianTeamId: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update Atlassian team in plan

HTTP PUT /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}
Path params:
  - planId (int)
  - atlassianTeamId (str)
Body: application/json-patch+json (Dict[str, Any])"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json-patch+json')
        _path: Dict[str, Any] = {'planId': planId, 'atlassianTeamId': atlassianTeamId}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_plan_only_team(self, planId: int, name: str, planningStyle: str, capacity: Optional[float]=None, issueSourceId: Optional[int]=None, memberAccountIds: Optional[list[str]]=None, sprintLength: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create plan-only team

HTTP POST /rest/api/3/plans/plan/{planId}/team/planonly
Path params:
  - planId (int)
Body (application/json) fields:
  - capacity (float, optional)
  - issueSourceId (int, optional)
  - memberAccountIds (list[str], optional)
  - name (str, required)
  - planningStyle (str, required)
  - sprintLength (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if capacity is not None:
            _body['capacity'] = capacity
        if issueSourceId is not None:
            _body['issueSourceId'] = issueSourceId
        if memberAccountIds is not None:
            _body['memberAccountIds'] = memberAccountIds
        _body['name'] = name
        _body['planningStyle'] = planningStyle
        if sprintLength is not None:
            _body['sprintLength'] = sprintLength
        rel_path = '/rest/api/3/plans/plan/{planId}/team/planonly'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_plan_only_team(self, planId: int, planOnlyTeamId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete plan-only team

HTTP DELETE /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}
Path params:
  - planId (int)
  - planOnlyTeamId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId, 'planOnlyTeamId': planOnlyTeamId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_plan_only_team(self, planId: int, planOnlyTeamId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get plan-only team

HTTP GET /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}
Path params:
  - planId (int)
  - planOnlyTeamId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId, 'planOnlyTeamId': planOnlyTeamId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_plan_only_team(self, planId: int, planOnlyTeamId: int, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update plan-only team

HTTP PUT /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}
Path params:
  - planId (int)
  - planOnlyTeamId (int)
Body: application/json-patch+json (Dict[str, Any])"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json-patch+json')
        _path: Dict[str, Any] = {'planId': planId, 'planOnlyTeamId': planOnlyTeamId}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def trash_plan(self, planId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Trash plan

HTTP PUT /rest/api/3/plans/plan/{planId}/trash
Path params:
  - planId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'planId': planId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/plans/plan/{planId}/trash'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_priorities(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get priorities

HTTP GET /rest/api/3/priority"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/priority'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_priority(self, name: str, statusColor: str, avatarId: Optional[int]=None, description: Optional[str]=None, iconUrl: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create priority

HTTP POST /rest/api/3/priority
Body (application/json) fields:
  - avatarId (int, optional)
  - description (str, optional)
  - iconUrl (str, optional)
  - name (str, required)
  - statusColor (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if avatarId is not None:
            _body['avatarId'] = avatarId
        if description is not None:
            _body['description'] = description
        if iconUrl is not None:
            _body['iconUrl'] = iconUrl
        _body['name'] = name
        _body['statusColor'] = statusColor
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/priority'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_default_priority(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set default priority

HTTP PUT /rest/api/3/priority/default
Body (application/json) fields:
  - id (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['id'] = id
        rel_path = '/rest/api/3/priority/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def move_priorities(self, ids: list[str], after: Optional[str]=None, position: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Move priorities

HTTP PUT /rest/api/3/priority/move
Body (application/json) fields:
  - after (str, optional)
  - ids (list[str], required)
  - position (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if after is not None:
            _body['after'] = after
        _body['ids'] = ids
        if position is not None:
            _body['position'] = position
        rel_path = '/rest/api/3/priority/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_priorities(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, id: Optional[list[str]]=None, projectId: Optional[list[str]]=None, priorityName: Optional[str]=None, onlyDefault: Optional[bool]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search priorities

HTTP GET /rest/api/3/priority/search
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - id (list[str], optional)
  - projectId (list[str], optional)
  - priorityName (str, optional)
  - onlyDefault (bool, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if projectId is not None:
            _query['projectId'] = projectId
        if priorityName is not None:
            _query['priorityName'] = priorityName
        if onlyDefault is not None:
            _query['onlyDefault'] = onlyDefault
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/priority/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_priority(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete priority

HTTP DELETE /rest/api/3/priority/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/priority/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_priority(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get priority

HTTP GET /rest/api/3/priority/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/priority/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_priority(self, id: str, avatarId: Optional[int]=None, description: Optional[str]=None, iconUrl: Optional[str]=None, name: Optional[str]=None, statusColor: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update priority

HTTP PUT /rest/api/3/priority/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - avatarId (int, optional)
  - description (str, optional)
  - iconUrl (str, optional)
  - name (str, optional)
  - statusColor (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if avatarId is not None:
            _body['avatarId'] = avatarId
        if description is not None:
            _body['description'] = description
        if iconUrl is not None:
            _body['iconUrl'] = iconUrl
        if name is not None:
            _body['name'] = name
        if statusColor is not None:
            _body['statusColor'] = statusColor
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/priority/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_priority_schemes(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, priorityId: Optional[list[int]]=None, schemeId: Optional[list[int]]=None, schemeName: Optional[str]=None, onlyDefault: Optional[bool]=None, orderBy: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get priority schemes

HTTP GET /rest/api/3/priorityscheme
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - priorityId (list[int], optional)
  - schemeId (list[int], optional)
  - schemeName (str, optional)
  - onlyDefault (bool, optional)
  - orderBy (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if priorityId is not None:
            _query['priorityId'] = priorityId
        if schemeId is not None:
            _query['schemeId'] = schemeId
        if schemeName is not None:
            _query['schemeName'] = schemeName
        if onlyDefault is not None:
            _query['onlyDefault'] = onlyDefault
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/priorityscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_priority_scheme(self, defaultPriorityId: int, name: str, priorityIds: list[int], description: Optional[str]=None, mappings: Optional[Dict[str, Any]]=None, projectIds: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create priority scheme

HTTP POST /rest/api/3/priorityscheme
Body (application/json) fields:
  - defaultPriorityId (int, required)
  - description (str, optional)
  - mappings (Dict[str, Any], optional)
  - name (str, required)
  - priorityIds (list[int], required)
  - projectIds (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['defaultPriorityId'] = defaultPriorityId
        if description is not None:
            _body['description'] = description
        if mappings is not None:
            _body['mappings'] = mappings
        _body['name'] = name
        _body['priorityIds'] = priorityIds
        if projectIds is not None:
            _body['projectIds'] = projectIds
        rel_path = '/rest/api/3/priorityscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def suggested_priorities_for_mappings(self, maxResults: Optional[int]=None, priorities: Optional[Dict[str, Any]]=None, projects: Optional[Dict[str, Any]]=None, schemeId: Optional[int]=None, startAt: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Suggested priorities for mappings

HTTP POST /rest/api/3/priorityscheme/mappings
Body (application/json) fields:
  - maxResults (int, optional)
  - priorities (Dict[str, Any], optional)
  - projects (Dict[str, Any], optional)
  - schemeId (int, optional)
  - startAt (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if maxResults is not None:
            _body['maxResults'] = maxResults
        if priorities is not None:
            _body['priorities'] = priorities
        if projects is not None:
            _body['projects'] = projects
        if schemeId is not None:
            _body['schemeId'] = schemeId
        if startAt is not None:
            _body['startAt'] = startAt
        rel_path = '/rest/api/3/priorityscheme/mappings'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_available_priorities_by_priority_scheme(self, schemeId: str, startAt: Optional[str]=None, maxResults: Optional[str]=None, query: Optional[str]=None, exclude: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get available priorities by priority scheme

HTTP GET /rest/api/3/priorityscheme/priorities/available
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - query (str, optional)
  - schemeId (str, required)
  - exclude (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if query is not None:
            _query['query'] = query
        _query['schemeId'] = schemeId
        if exclude is not None:
            _query['exclude'] = exclude
        _body = None
        rel_path = '/rest/api/3/priorityscheme/priorities/available'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_priority_scheme(self, schemeId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete priority scheme

HTTP DELETE /rest/api/3/priorityscheme/{schemeId}
Path params:
  - schemeId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/priorityscheme/{schemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_priority_scheme(self, schemeId: int, defaultPriorityId: Optional[int]=None, description: Optional[str]=None, mappings: Optional[Dict[str, Any]]=None, name: Optional[str]=None, priorities: Optional[Dict[str, Any]]=None, projects: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update priority scheme

HTTP PUT /rest/api/3/priorityscheme/{schemeId}
Path params:
  - schemeId (int)
Body (application/json) fields:
  - defaultPriorityId (int, optional)
  - description (str, optional)
  - mappings (Dict[str, Any], optional)
  - name (str, optional)
  - priorities (Dict[str, Any], optional)
  - projects (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultPriorityId is not None:
            _body['defaultPriorityId'] = defaultPriorityId
        if description is not None:
            _body['description'] = description
        if mappings is not None:
            _body['mappings'] = mappings
        if name is not None:
            _body['name'] = name
        if priorities is not None:
            _body['priorities'] = priorities
        if projects is not None:
            _body['projects'] = projects
        rel_path = '/rest/api/3/priorityscheme/{schemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_priorities_by_priority_scheme(self, schemeId: str, startAt: Optional[str]=None, maxResults: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get priorities by priority scheme

HTTP GET /rest/api/3/priorityscheme/{schemeId}/priorities
Path params:
  - schemeId (str)
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/priorityscheme/{schemeId}/priorities'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_projects_by_priority_scheme(self, schemeId: str, startAt: Optional[str]=None, maxResults: Optional[str]=None, projectId: Optional[list[int]]=None, query: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get projects by priority scheme

HTTP GET /rest/api/3/priorityscheme/{schemeId}/projects
Path params:
  - schemeId (str)
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - projectId (list[int], optional)
  - query (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'schemeId': schemeId}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if projectId is not None:
            _query['projectId'] = projectId
        if query is not None:
            _query['query'] = query
        _body = None
        rel_path = '/rest/api/3/priorityscheme/{schemeId}/projects'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_projects(self, expand: Optional[str]=None, recent: Optional[int]=None, properties: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all projects

HTTP GET /rest/api/3/project
Query params:
  - expand (str, optional)
  - recent (int, optional)
  - properties (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if recent is not None:
            _query['recent'] = recent
        if properties is not None:
            _query['properties'] = properties
        _body = None
        rel_path = '/rest/api/3/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_project(self, key: str, name: str, assigneeType: Optional[str]=None, avatarId: Optional[int]=None, categoryId: Optional[int]=None, description: Optional[str]=None, fieldConfigurationScheme: Optional[int]=None, issueSecurityScheme: Optional[int]=None, issueTypeScheme: Optional[int]=None, issueTypeScreenScheme: Optional[int]=None, lead: Optional[str]=None, leadAccountId: Optional[str]=None, notificationScheme: Optional[int]=None, permissionScheme: Optional[int]=None, projectTemplateKey: Optional[str]=None, projectTypeKey: Optional[str]=None, url: Optional[str]=None, workflowScheme: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create project

HTTP POST /rest/api/3/project
Body (application/json) fields:
  - assigneeType (str, optional)
  - avatarId (int, optional)
  - categoryId (int, optional)
  - description (str, optional)
  - fieldConfigurationScheme (int, optional)
  - issueSecurityScheme (int, optional)
  - issueTypeScheme (int, optional)
  - issueTypeScreenScheme (int, optional)
  - key (str, required)
  - lead (str, optional)
  - leadAccountId (str, optional)
  - name (str, required)
  - notificationScheme (int, optional)
  - permissionScheme (int, optional)
  - projectTemplateKey (str, optional)
  - projectTypeKey (str, optional)
  - url (str, optional)
  - workflowScheme (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if assigneeType is not None:
            _body['assigneeType'] = assigneeType
        if avatarId is not None:
            _body['avatarId'] = avatarId
        if categoryId is not None:
            _body['categoryId'] = categoryId
        if description is not None:
            _body['description'] = description
        if fieldConfigurationScheme is not None:
            _body['fieldConfigurationScheme'] = fieldConfigurationScheme
        if issueSecurityScheme is not None:
            _body['issueSecurityScheme'] = issueSecurityScheme
        if issueTypeScheme is not None:
            _body['issueTypeScheme'] = issueTypeScheme
        if issueTypeScreenScheme is not None:
            _body['issueTypeScreenScheme'] = issueTypeScreenScheme
        _body['key'] = key
        if lead is not None:
            _body['lead'] = lead
        if leadAccountId is not None:
            _body['leadAccountId'] = leadAccountId
        _body['name'] = name
        if notificationScheme is not None:
            _body['notificationScheme'] = notificationScheme
        if permissionScheme is not None:
            _body['permissionScheme'] = permissionScheme
        if projectTemplateKey is not None:
            _body['projectTemplateKey'] = projectTemplateKey
        if projectTypeKey is not None:
            _body['projectTypeKey'] = projectTypeKey
        if url is not None:
            _body['url'] = url
        if workflowScheme is not None:
            _body['workflowScheme'] = workflowScheme
        rel_path = '/rest/api/3/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_project_with_custom_template(self, details: Optional[Dict[str, Any]]=None, template: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create custom project

HTTP POST /rest/api/3/project-template
Body (application/json) fields:
  - details (Dict[str, Any], optional)
  - template (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if details is not None:
            _body['details'] = details
        if template is not None:
            _body['template'] = template
        rel_path = '/rest/api/3/project-template'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def edit_template(self, templateDescription: Optional[str]=None, templateGenerationOptions: Optional[Dict[str, Any]]=None, templateKey: Optional[str]=None, templateName: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Edit a custom project template

HTTP PUT /rest/api/3/project-template/edit-template
Body (application/json) fields:
  - templateDescription (str, optional)
  - templateGenerationOptions (Dict[str, Any], optional)
  - templateKey (str, optional)
  - templateName (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if templateDescription is not None:
            _body['templateDescription'] = templateDescription
        if templateGenerationOptions is not None:
            _body['templateGenerationOptions'] = templateGenerationOptions
        if templateKey is not None:
            _body['templateKey'] = templateKey
        if templateName is not None:
            _body['templateName'] = templateName
        rel_path = '/rest/api/3/project-template/edit-template'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def live_template(self, projectId: Optional[str]=None, templateKey: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Gets a custom project template

HTTP GET /rest/api/3/project-template/live-template
Query params:
  - projectId (str, optional)
  - templateKey (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if projectId is not None:
            _query['projectId'] = projectId
        if templateKey is not None:
            _query['templateKey'] = templateKey
        _body = None
        rel_path = '/rest/api/3/project-template/live-template'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_template(self, templateKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Deletes a custom project template

HTTP DELETE /rest/api/3/project-template/remove-template
Query params:
  - templateKey (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['templateKey'] = templateKey
        _body = None
        rel_path = '/rest/api/3/project-template/remove-template'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def save_template(self, templateDescription: Optional[str]=None, templateFromProjectRequest: Optional[Dict[str, Any]]=None, templateName: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Save a custom project template

HTTP POST /rest/api/3/project-template/save-template
Body (application/json) fields:
  - templateDescription (str, optional)
  - templateFromProjectRequest (Dict[str, Any], optional)
  - templateName (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if templateDescription is not None:
            _body['templateDescription'] = templateDescription
        if templateFromProjectRequest is not None:
            _body['templateFromProjectRequest'] = templateFromProjectRequest
        if templateName is not None:
            _body['templateName'] = templateName
        rel_path = '/rest/api/3/project-template/save-template'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_recent(self, expand: Optional[str]=None, properties: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get recent projects

HTTP GET /rest/api/3/project/recent
Query params:
  - expand (str, optional)
  - properties (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if properties is not None:
            _query['properties'] = properties
        _body = None
        rel_path = '/rest/api/3/project/recent'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_projects(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, orderBy: Optional[str]=None, id: Optional[list[int]]=None, keys: Optional[list[str]]=None, query: Optional[str]=None, typeKey: Optional[str]=None, categoryId: Optional[int]=None, action: Optional[str]=None, expand: Optional[str]=None, status: Optional[list[str]]=None, properties: Optional[list[Dict[str, Any]]]=None, propertyQuery: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get projects paginated

HTTP GET /rest/api/3/project/search
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - orderBy (str, optional)
  - id (list[int], optional)
  - keys (list[str], optional)
  - query (str, optional)
  - typeKey (str, optional)
  - categoryId (int, optional)
  - action (str, optional)
  - expand (str, optional)
  - status (list[str], optional)
  - properties (list[Dict[str, Any]], optional)
  - propertyQuery (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if id is not None:
            _query['id'] = id
        if keys is not None:
            _query['keys'] = keys
        if query is not None:
            _query['query'] = query
        if typeKey is not None:
            _query['typeKey'] = typeKey
        if categoryId is not None:
            _query['categoryId'] = categoryId
        if action is not None:
            _query['action'] = action
        if expand is not None:
            _query['expand'] = expand
        if status is not None:
            _query['status'] = status
        if properties is not None:
            _query['properties'] = properties
        if propertyQuery is not None:
            _query['propertyQuery'] = propertyQuery
        _body = None
        rel_path = '/rest/api/3/project/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_project_types(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all project types

HTTP GET /rest/api/3/project/type"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/type'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_accessible_project_types(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get licensed project types

HTTP GET /rest/api/3/project/type/accessible"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/type/accessible'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_type_by_key(self, projectTypeKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project type by key

HTTP GET /rest/api/3/project/type/{projectTypeKey}
Path params:
  - projectTypeKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectTypeKey': projectTypeKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/type/{projectTypeKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_accessible_project_type_by_key(self, projectTypeKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get accessible project type by key

HTTP GET /rest/api/3/project/type/{projectTypeKey}/accessible
Path params:
  - projectTypeKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectTypeKey': projectTypeKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/type/{projectTypeKey}/accessible'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_project(self, projectIdOrKey: str, enableUndo: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete project

HTTP DELETE /rest/api/3/project/{projectIdOrKey}
Path params:
  - projectIdOrKey (str)
Query params:
  - enableUndo (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if enableUndo is not None:
            _query['enableUndo'] = enableUndo
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project(self, projectIdOrKey: str, expand: Optional[str]=None, properties: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project

HTTP GET /rest/api/3/project/{projectIdOrKey}
Path params:
  - projectIdOrKey (str)
Query params:
  - expand (str, optional)
  - properties (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        if properties is not None:
            _query['properties'] = properties
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_project(self, projectIdOrKey: str, expand: Optional[str]=None, assigneeType: Optional[str]=None, avatarId: Optional[int]=None, categoryId: Optional[int]=None, description: Optional[str]=None, issueSecurityScheme: Optional[int]=None, key: Optional[str]=None, lead: Optional[str]=None, leadAccountId: Optional[str]=None, name: Optional[str]=None, notificationScheme: Optional[int]=None, permissionScheme: Optional[int]=None, releasedProjectKeys: Optional[list[str]]=None, url: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update project

HTTP PUT /rest/api/3/project/{projectIdOrKey}
Path params:
  - projectIdOrKey (str)
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - assigneeType (str, optional)
  - avatarId (int, optional)
  - categoryId (int, optional)
  - description (str, optional)
  - issueSecurityScheme (int, optional)
  - key (str, optional)
  - lead (str, optional)
  - leadAccountId (str, optional)
  - name (str, optional)
  - notificationScheme (int, optional)
  - permissionScheme (int, optional)
  - releasedProjectKeys (list[str], optional)
  - url (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        if assigneeType is not None:
            _body['assigneeType'] = assigneeType
        if avatarId is not None:
            _body['avatarId'] = avatarId
        if categoryId is not None:
            _body['categoryId'] = categoryId
        if description is not None:
            _body['description'] = description
        if issueSecurityScheme is not None:
            _body['issueSecurityScheme'] = issueSecurityScheme
        if key is not None:
            _body['key'] = key
        if lead is not None:
            _body['lead'] = lead
        if leadAccountId is not None:
            _body['leadAccountId'] = leadAccountId
        if name is not None:
            _body['name'] = name
        if notificationScheme is not None:
            _body['notificationScheme'] = notificationScheme
        if permissionScheme is not None:
            _body['permissionScheme'] = permissionScheme
        if releasedProjectKeys is not None:
            _body['releasedProjectKeys'] = releasedProjectKeys
        if url is not None:
            _body['url'] = url
        rel_path = '/rest/api/3/project/{projectIdOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def archive_project(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Archive project

HTTP POST /rest/api/3/project/{projectIdOrKey}/archive
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/archive'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_project_avatar(self, projectIdOrKey: str, id: str, fileName: Optional[str]=None, isDeletable: Optional[bool]=None, isSelected: Optional[bool]=None, isSystemAvatar: Optional[bool]=None, owner: Optional[str]=None, urls: Optional[Dict[str, Any]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set project avatar

HTTP PUT /rest/api/3/project/{projectIdOrKey}/avatar
Path params:
  - projectIdOrKey (str)
Body (application/json) fields:
  - fileName (str, optional)
  - id (str, required)
  - isDeletable (bool, optional)
  - isSelected (bool, optional)
  - isSystemAvatar (bool, optional)
  - owner (str, optional)
  - urls (Dict[str, Any], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if fileName is not None:
            _body['fileName'] = fileName
        _body['id'] = id
        if isDeletable is not None:
            _body['isDeletable'] = isDeletable
        if isSelected is not None:
            _body['isSelected'] = isSelected
        if isSystemAvatar is not None:
            _body['isSystemAvatar'] = isSystemAvatar
        if owner is not None:
            _body['owner'] = owner
        if urls is not None:
            _body['urls'] = urls
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/project/{projectIdOrKey}/avatar'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_project_avatar(self, projectIdOrKey: str, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete project avatar

HTTP DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id}
Path params:
  - projectIdOrKey (str)
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/avatar/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_project_avatar(self, projectIdOrKey: str, x: Optional[int]=None, y: Optional[int]=None, size: Optional[int]=None, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Load project avatar

HTTP POST /rest/api/3/project/{projectIdOrKey}/avatar2
Path params:
  - projectIdOrKey (str)
Query params:
  - x (int, optional)
  - y (int, optional)
  - size (int, optional)
Body: */* (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', '*/*')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if x is not None:
            _query['x'] = x
        if y is not None:
            _query['y'] = y
        if size is not None:
            _query['size'] = size
        _body = body
        rel_path = '/rest/api/3/project/{projectIdOrKey}/avatar2'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_project_avatars(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all project avatars

HTTP GET /rest/api/3/project/{projectIdOrKey}/avatars
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/avatars'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_default_project_classification(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove the default data classification level from a project

HTTP DELETE /rest/api/3/project/{projectIdOrKey}/classification-level/default
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/classification-level/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_default_project_classification(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get the default data classification level of a project

HTTP GET /rest/api/3/project/{projectIdOrKey}/classification-level/default
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/classification-level/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_default_project_classification(self, projectIdOrKey: str, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update the default data classification level of a project

HTTP PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default
Path params:
  - projectIdOrKey (str)
Body (application/json) fields:
  - id (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['id'] = id
        rel_path = '/rest/api/3/project/{projectIdOrKey}/classification-level/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_components_paginated(self, projectIdOrKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, orderBy: Optional[str]=None, componentSource: Optional[str]=None, query: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project components paginated

HTTP GET /rest/api/3/project/{projectIdOrKey}/component
Path params:
  - projectIdOrKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - orderBy (str, optional)
  - componentSource (str, optional)
  - query (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if componentSource is not None:
            _query['componentSource'] = componentSource
        if query is not None:
            _query['query'] = query
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/component'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_components(self, projectIdOrKey: str, componentSource: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project components

HTTP GET /rest/api/3/project/{projectIdOrKey}/components
Path params:
  - projectIdOrKey (str)
Query params:
  - componentSource (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if componentSource is not None:
            _query['componentSource'] = componentSource
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/components'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_project_asynchronously(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete project asynchronously

HTTP POST /rest/api/3/project/{projectIdOrKey}/delete
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/delete'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_features_for_project(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project features

HTTP GET /rest/api/3/project/{projectIdOrKey}/features
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        rel_path = '/rest/api/3/project/{projectIdOrKey}/features'
        # Since only one header dict conversion is needed, perform conversion only if headers provided
        _headers = headers if headers is not None else {}
        _path = {'projectIdOrKey': projectIdOrKey}

        url = self.base_url + _safe_format_url(rel_path, _path)

        # Pre-stringify dict fields before HTTPRequest construction (reduces repeated comprehensions)
        headers_str = _as_str_dict(_headers)
        path_str = _as_str_dict(_path)
        # _query is always empty dict here, so avoid constructing each time
        empty_query_str = {}

        req = HTTPRequest(
            method='GET',
            url=url,
            headers=headers_str,
            path_params=path_str,
            query_params=empty_query_str,  # Previously _as_str_dict(_query) for empty dict every time
            body=None,
        )
        resp = await self._client.execute(req)
        return resp

    async def toggle_feature_for_project(self, projectIdOrKey: str, featureKey: str, state: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set project feature state

HTTP PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey}
Path params:
  - projectIdOrKey (str)
  - featureKey (str)
Body (application/json) fields:
  - state (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'featureKey': featureKey}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if state is not None:
            _body['state'] = state
        rel_path = '/rest/api/3/project/{projectIdOrKey}/features/{featureKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_property_keys(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project property keys

HTTP GET /rest/api/3/project/{projectIdOrKey}/properties
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_project_property(self, projectIdOrKey: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete project property

HTTP DELETE /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}
Path params:
  - projectIdOrKey (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_property(self, projectIdOrKey: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project property

HTTP GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}
Path params:
  - projectIdOrKey (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_project_property(self, projectIdOrKey: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set project property

HTTP PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}
Path params:
  - projectIdOrKey (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def restore(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Restore deleted or archived project

HTTP POST /rest/api/3/project/{projectIdOrKey}/restore
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/restore'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_roles(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project roles for project

HTTP GET /rest/api/3/project/{projectIdOrKey}/role
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/role'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_actor(self, projectIdOrKey: str, id: int, user: Optional[str]=None, group: Optional[str]=None, groupId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete actors from project role

HTTP DELETE /rest/api/3/project/{projectIdOrKey}/role/{id}
Path params:
  - projectIdOrKey (str)
  - id (int)
Query params:
  - user (str, optional)
  - group (str, optional)
  - groupId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if user is not None:
            _query['user'] = user
        if group is not None:
            _query['group'] = group
        if groupId is not None:
            _query['groupId'] = groupId
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_role(self, projectIdOrKey: str, id: int, excludeInactiveUsers: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project role for project

HTTP GET /rest/api/3/project/{projectIdOrKey}/role/{id}
Path params:
  - projectIdOrKey (str)
  - id (int)
Query params:
  - excludeInactiveUsers (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        if excludeInactiveUsers is not None:
            _query['excludeInactiveUsers'] = excludeInactiveUsers
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_actor_users(self, projectIdOrKey: str, id: int, group: Optional[list[str]]=None, groupId: Optional[list[str]]=None, user: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add actors to project role

HTTP POST /rest/api/3/project/{projectIdOrKey}/role/{id}
Path params:
  - projectIdOrKey (str)
  - id (int)
Body (application/json) fields:
  - group (list[str], optional)
  - groupId (list[str], optional)
  - user (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if group is not None:
            _body['group'] = group
        if groupId is not None:
            _body['groupId'] = groupId
        if user is not None:
            _body['user'] = user
        rel_path = '/rest/api/3/project/{projectIdOrKey}/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_actors(self, projectIdOrKey: str, id: int, categorisedActors: Optional[Dict[str, Any]]=None, id_body: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set actors for project role

HTTP PUT /rest/api/3/project/{projectIdOrKey}/role/{id}
Path params:
  - projectIdOrKey (str)
  - id (int)
Body (application/json) fields:
  - categorisedActors (Dict[str, Any], optional)
  - id (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey, 'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if categorisedActors is not None:
            _body['categorisedActors'] = categorisedActors
        if id_body is not None:
            _body['id'] = id_body
        rel_path = '/rest/api/3/project/{projectIdOrKey}/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_role_details(self, projectIdOrKey: str, currentMember: Optional[bool]=None, excludeConnectAddons: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project role details

HTTP GET /rest/api/3/project/{projectIdOrKey}/roledetails
Path params:
  - projectIdOrKey (str)
Query params:
  - currentMember (bool, optional)
  - excludeConnectAddons (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if currentMember is not None:
            _query['currentMember'] = currentMember
        if excludeConnectAddons is not None:
            _query['excludeConnectAddons'] = excludeConnectAddons
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/roledetails'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_statuses(self, projectIdOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all statuses for project

HTTP GET /rest/api/3/project/{projectIdOrKey}/statuses
Path params:
  - projectIdOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/statuses'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_versions_paginated(self, projectIdOrKey: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, orderBy: Optional[str]=None, query: Optional[str]=None, status: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project versions paginated

HTTP GET /rest/api/3/project/{projectIdOrKey}/version
Path params:
  - projectIdOrKey (str)
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - orderBy (str, optional)
  - query (str, optional)
  - status (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if query is not None:
            _query['query'] = query
        if status is not None:
            _query['status'] = status
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/version'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_versions(self, projectIdOrKey: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project versions

HTTP GET /rest/api/3/project/{projectIdOrKey}/versions
Path params:
  - projectIdOrKey (str)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectIdOrKey': projectIdOrKey}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/project/{projectIdOrKey}/versions'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_email(self, projectId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project's sender email

HTTP GET /rest/api/3/project/{projectId}/email
Path params:
  - projectId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectId': projectId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectId}/email'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_project_email(self, projectId: int, emailAddress: Optional[str]=None, emailAddressStatus: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set project's sender email

HTTP PUT /rest/api/3/project/{projectId}/email
Path params:
  - projectId (int)
Body (application/json) fields:
  - emailAddress (str, optional)
  - emailAddressStatus (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectId': projectId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if emailAddress is not None:
            _body['emailAddress'] = emailAddress
        if emailAddressStatus is not None:
            _body['emailAddressStatus'] = emailAddressStatus
        rel_path = '/rest/api/3/project/{projectId}/email'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_hierarchy(self, projectId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project issue type hierarchy

HTTP GET /rest/api/3/project/{projectId}/hierarchy
Path params:
  - projectId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectId': projectId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectId}/hierarchy'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_issue_security_scheme(self, projectKeyOrId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project issue security scheme

HTTP GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme
Path params:
  - projectKeyOrId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectKeyOrId': projectKeyOrId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_notification_scheme_for_project(self, projectKeyOrId: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project notification scheme

HTTP GET /rest/api/3/project/{projectKeyOrId}/notificationscheme
Path params:
  - projectKeyOrId (str)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectKeyOrId': projectKeyOrId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/project/{projectKeyOrId}/notificationscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_assigned_permission_scheme(self, projectKeyOrId: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get assigned permission scheme

HTTP GET /rest/api/3/project/{projectKeyOrId}/permissionscheme
Path params:
  - projectKeyOrId (str)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectKeyOrId': projectKeyOrId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/project/{projectKeyOrId}/permissionscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_permission_scheme(self, projectKeyOrId: str, id: int, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign permission scheme

HTTP PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme
Path params:
  - projectKeyOrId (str)
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - id (int, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'projectKeyOrId': projectKeyOrId}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        _body['id'] = id
        rel_path = '/rest/api/3/project/{projectKeyOrId}/permissionscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_security_levels_for_project(self, projectKeyOrId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project issue security levels

HTTP GET /rest/api/3/project/{projectKeyOrId}/securitylevel
Path params:
  - projectKeyOrId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'projectKeyOrId': projectKeyOrId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/project/{projectKeyOrId}/securitylevel'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_project_categories(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all project categories

HTTP GET /rest/api/3/projectCategory"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/projectCategory'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_project_category(self, description: Optional[str]=None, id: Optional[str]=None, name: Optional[str]=None, self_: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create project category

HTTP POST /rest/api/3/projectCategory
Body (application/json) fields:
  - description (str, optional)
  - id (str, optional)
  - name (str, optional)
  - self (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if id is not None:
            _body['id'] = id
        if name is not None:
            _body['name'] = name
        if self_ is not None:
            _body['self'] = self_
        rel_path = '/rest/api/3/projectCategory'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_project_category(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete project category

HTTP DELETE /rest/api/3/projectCategory/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/projectCategory/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_category_by_id(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project category by ID

HTTP GET /rest/api/3/projectCategory/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/projectCategory/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_project_category(self, id: int, description: Optional[str]=None, id_body: Optional[str]=None, name: Optional[str]=None, self_: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update project category

HTTP PUT /rest/api/3/projectCategory/{id}
Path params:
  - id (int)
Body (application/json) fields:
  - description (str, optional)
  - id (str, optional)
  - name (str, optional)
  - self (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if id_body is not None:
            _body['id'] = id_body
        if name is not None:
            _body['name'] = name
        if self_ is not None:
            _body['self'] = self_
        rel_path = '/rest/api/3/projectCategory/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def validate_project_key(self, key: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Validate project key

HTTP GET /rest/api/3/projectvalidate/key
Query params:
  - key (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if key is not None:
            _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/projectvalidate/key'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_valid_project_key(self, key: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get valid project key

HTTP GET /rest/api/3/projectvalidate/validProjectKey
Query params:
  - key (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if key is not None:
            _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/projectvalidate/validProjectKey'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_valid_project_name(self, name: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get valid project name

HTTP GET /rest/api/3/projectvalidate/validProjectName
Query params:
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['name'] = name
        _body = None
        rel_path = '/rest/api/3/projectvalidate/validProjectName'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def redact(self, redactions: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Redact

HTTP POST /rest/api/3/redact
Body (application/json) fields:
  - redactions (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if redactions is not None:
            _body['redactions'] = redactions
        rel_path = '/rest/api/3/redact'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_redaction_status(self, jobId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get redaction status

HTTP GET /rest/api/3/redact/status/{jobId}
Path params:
  - jobId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'jobId': jobId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/redact/status/{jobId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_resolutions(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get resolutions

HTTP GET /rest/api/3/resolution"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/resolution'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_resolution(self, name: str, description: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create resolution

HTTP POST /rest/api/3/resolution
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/resolution'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_default_resolution(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set default resolution

HTTP PUT /rest/api/3/resolution/default
Body (application/json) fields:
  - id (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['id'] = id
        rel_path = '/rest/api/3/resolution/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def move_resolutions(self, ids: list[str], after: Optional[str]=None, position: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Move resolutions

HTTP PUT /rest/api/3/resolution/move
Body (application/json) fields:
  - after (str, optional)
  - ids (list[str], required)
  - position (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if after is not None:
            _body['after'] = after
        _body['ids'] = ids
        if position is not None:
            _body['position'] = position
        rel_path = '/rest/api/3/resolution/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_resolutions(self, startAt: Optional[str]=None, maxResults: Optional[str]=None, id: Optional[list[str]]=None, onlyDefault: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search resolutions

HTTP GET /rest/api/3/resolution/search
Query params:
  - startAt (str, optional)
  - maxResults (str, optional)
  - id (list[str], optional)
  - onlyDefault (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if onlyDefault is not None:
            _query['onlyDefault'] = onlyDefault
        _body = None
        rel_path = '/rest/api/3/resolution/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_resolution(self, id: str, replaceWith: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete resolution

HTTP DELETE /rest/api/3/resolution/{id}
Path params:
  - id (str)
Query params:
  - replaceWith (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _query['replaceWith'] = replaceWith
        _body = None
        rel_path = '/rest/api/3/resolution/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_resolution(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get resolution

HTTP GET /rest/api/3/resolution/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/resolution/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_resolution(self, id: str, name: str, description: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update resolution

HTTP PUT /rest/api/3/resolution/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/resolution/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_project_roles(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all project roles

HTTP GET /rest/api/3/role"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/role'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_project_role(self, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create project role

HTTP POST /rest/api/3/role
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/role'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_project_role(self, id: int, swap: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete project role

HTTP DELETE /rest/api/3/role/{id}
Path params:
  - id (int)
Query params:
  - swap (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if swap is not None:
            _query['swap'] = swap
        _body = None
        rel_path = '/rest/api/3/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_role_by_id(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project role by ID

HTTP GET /rest/api/3/role/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def partial_update_project_role(self, id: int, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Partial update project role

HTTP POST /rest/api/3/role/{id}
Path params:
  - id (int)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def fully_update_project_role(self, id: int, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Fully update project role

HTTP PUT /rest/api/3/role/{id}
Path params:
  - id (int)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/role/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_project_role_actors_from_role(self, id: int, user: Optional[str]=None, groupId: Optional[str]=None, group: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete default actors from project role

HTTP DELETE /rest/api/3/role/{id}/actors
Path params:
  - id (int)
Query params:
  - user (str, optional)
  - groupId (str, optional)
  - group (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if user is not None:
            _query['user'] = user
        if groupId is not None:
            _query['groupId'] = groupId
        if group is not None:
            _query['group'] = group
        _body = None
        rel_path = '/rest/api/3/role/{id}/actors'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_role_actors_for_role(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get default actors for project role

HTTP GET /rest/api/3/role/{id}/actors
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/role/{id}/actors'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_project_role_actors_to_role(self, id: int, group: Optional[list[str]]=None, groupId: Optional[list[str]]=None, user: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add default actors to project role

HTTP POST /rest/api/3/role/{id}/actors
Path params:
  - id (int)
Body (application/json) fields:
  - group (list[str], optional)
  - groupId (list[str], optional)
  - user (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if group is not None:
            _body['group'] = group
        if groupId is not None:
            _body['groupId'] = groupId
        if user is not None:
            _body['user'] = user
        rel_path = '/rest/api/3/role/{id}/actors'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_screens(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[int]]=None, queryString: Optional[str]=None, scope: Optional[list[str]]=None, orderBy: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get screens

HTTP GET /rest/api/3/screens
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[int], optional)
  - queryString (str, optional)
  - scope (list[str], optional)
  - orderBy (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if queryString is not None:
            _query['queryString'] = queryString
        if scope is not None:
            _query['scope'] = scope
        if orderBy is not None:
            _query['orderBy'] = orderBy
        _body = None
        rel_path = '/rest/api/3/screens'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_screen(self, name: str, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create screen

HTTP POST /rest/api/3/screens
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        rel_path = '/rest/api/3/screens'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_field_to_default_screen(self, fieldId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add field to default screen

HTTP POST /rest/api/3/screens/addToDefault/{fieldId}
Path params:
  - fieldId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'fieldId': fieldId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screens/addToDefault/{fieldId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_bulk_screen_tabs(self, screenId: Optional[list[int]]=None, tabId: Optional[list[int]]=None, startAt: Optional[int]=None, maxResult: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get bulk screen tabs

HTTP GET /rest/api/3/screens/tabs
Query params:
  - screenId (list[int], optional)
  - tabId (list[int], optional)
  - startAt (int, optional)
  - maxResult (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if screenId is not None:
            _query['screenId'] = screenId
        if tabId is not None:
            _query['tabId'] = tabId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResult is not None:
            _query['maxResult'] = maxResult
        _body = None
        rel_path = '/rest/api/3/screens/tabs'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_screen(self, screenId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete screen

HTTP DELETE /rest/api/3/screens/{screenId}
Path params:
  - screenId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_screen(self, screenId: int, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update screen

HTTP PUT /rest/api/3/screens/{screenId}
Path params:
  - screenId (int)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'screenId': screenId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/screens/{screenId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_available_screen_fields(self, screenId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get available screen fields

HTTP GET /rest/api/3/screens/{screenId}/availableFields
Path params:
  - screenId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}/availableFields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_screen_tabs(self, screenId: int, projectKey: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all screen tabs

HTTP GET /rest/api/3/screens/{screenId}/tabs
Path params:
  - screenId (int)
Query params:
  - projectKey (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId}
        _query: Dict[str, Any] = {}
        if projectKey is not None:
            _query['projectKey'] = projectKey
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}/tabs'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_screen_tab(self, screenId: int, name: str, id: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create screen tab

HTTP POST /rest/api/3/screens/{screenId}/tabs
Path params:
  - screenId (int)
Body (application/json) fields:
  - id (int, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'screenId': screenId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if id is not None:
            _body['id'] = id
        _body['name'] = name
        rel_path = '/rest/api/3/screens/{screenId}/tabs'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_screen_tab(self, screenId: int, tabId: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete screen tab

HTTP DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}
Path params:
  - screenId (int)
  - tabId (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def rename_screen_tab(self, screenId: int, tabId: int, name: str, id: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update screen tab

HTTP PUT /rest/api/3/screens/{screenId}/tabs/{tabId}
Path params:
  - screenId (int)
  - tabId (int)
Body (application/json) fields:
  - id (int, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if id is not None:
            _body['id'] = id
        _body['name'] = name
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_screen_tab_fields(self, screenId: int, tabId: int, projectKey: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all screen tab fields

HTTP GET /rest/api/3/screens/{screenId}/tabs/{tabId}/fields
Path params:
  - screenId (int)
  - tabId (int)
Query params:
  - projectKey (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId}
        _query: Dict[str, Any] = {}
        if projectKey is not None:
            _query['projectKey'] = projectKey
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def add_screen_tab_field(self, screenId: int, tabId: int, fieldId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Add screen tab field

HTTP POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields
Path params:
  - screenId (int)
  - tabId (int)
Body (application/json) fields:
  - fieldId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['fieldId'] = fieldId
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_screen_tab_field(self, screenId: int, tabId: int, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove screen tab field

HTTP DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}
Path params:
  - screenId (int)
  - tabId (int)
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId, 'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def move_screen_tab_field(self, screenId: int, tabId: int, id: str, after: Optional[str]=None, position: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Move screen tab field

HTTP POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move
Path params:
  - screenId (int)
  - tabId (int)
  - id (str)
Body (application/json) fields:
  - after (str, optional)
  - position (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId, 'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if after is not None:
            _body['after'] = after
        if position is not None:
            _body['position'] = position
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def move_screen_tab(self, screenId: int, tabId: int, pos: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Move screen tab

HTTP POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}
Path params:
  - screenId (int)
  - tabId (int)
  - pos (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenId': screenId, 'tabId': tabId, 'pos': pos}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_screen_schemes(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, id: Optional[list[int]]=None, expand: Optional[str]=None, queryString: Optional[str]=None, orderBy: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get screen schemes

HTTP GET /rest/api/3/screenscheme
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - id (list[int], optional)
  - expand (str, optional)
  - queryString (str, optional)
  - orderBy (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if id is not None:
            _query['id'] = id
        if expand is not None:
            _query['expand'] = expand
        if queryString is not None:
            _query['queryString'] = queryString
        if orderBy is not None:
            _query['orderBy'] = orderBy
        _body = None
        rel_path = '/rest/api/3/screenscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_screen_scheme(self, name: str, screens: Dict[str, Any], description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create screen scheme

HTTP POST /rest/api/3/screenscheme
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)
  - screens (Dict[str, Any], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        _body['screens'] = screens
        rel_path = '/rest/api/3/screenscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_screen_scheme(self, screenSchemeId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete screen scheme

HTTP DELETE /rest/api/3/screenscheme/{screenSchemeId}
Path params:
  - screenSchemeId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'screenSchemeId': screenSchemeId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/screenscheme/{screenSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_screen_scheme(self, screenSchemeId: str, description: Optional[str]=None, name: Optional[str]=None, screens: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update screen scheme

HTTP PUT /rest/api/3/screenscheme/{screenSchemeId}
Path params:
  - screenSchemeId (str)
Body (application/json) fields:
  - description (str, optional)
  - name (str, optional)
  - screens (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'screenSchemeId': screenSchemeId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        if screens is not None:
            _body['screens'] = screens
        rel_path = '/rest/api/3/screenscheme/{screenSchemeId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_for_issues_using_jql(self, jql: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, validateQuery: Optional[str]=None, fields: Optional[list[str]]=None, expand: Optional[str]=None, properties: Optional[list[str]]=None, fieldsByKeys: Optional[bool]=None, failFast: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Currently being removed. Search for issues using JQL (GET)

HTTP GET /rest/api/3/search
Query params:
  - jql (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - validateQuery (str, optional)
  - fields (list[str], optional)
  - expand (str, optional)
  - properties (list[str], optional)
  - fieldsByKeys (bool, optional)
  - failFast (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if jql is not None:
            _query['jql'] = jql
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if validateQuery is not None:
            _query['validateQuery'] = validateQuery
        if fields is not None:
            _query['fields'] = fields
        if expand is not None:
            _query['expand'] = expand
        if properties is not None:
            _query['properties'] = properties
        if fieldsByKeys is not None:
            _query['fieldsByKeys'] = fieldsByKeys
        if failFast is not None:
            _query['failFast'] = failFast
        _body = None
        rel_path = '/rest/api/3/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_for_issues_using_jql_post(self, expand: Optional[list[str]]=None, fields: Optional[list[str]]=None, fieldsByKeys: Optional[bool]=None, jql: Optional[str]=None, maxResults: Optional[int]=None, properties: Optional[list[str]]=None, startAt: Optional[int]=None, validateQuery: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Currently being removed. Search for issues using JQL (POST)

HTTP POST /rest/api/3/search
Body (application/json) fields:
  - expand (list[str], optional)
  - fields (list[str], optional)
  - fieldsByKeys (bool, optional)
  - jql (str, optional)
  - maxResults (int, optional)
  - properties (list[str], optional)
  - startAt (int, optional)
  - validateQuery (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if expand is not None:
            _body['expand'] = expand
        if fields is not None:
            _body['fields'] = fields
        if fieldsByKeys is not None:
            _body['fieldsByKeys'] = fieldsByKeys
        if jql is not None:
            _body['jql'] = jql
        if maxResults is not None:
            _body['maxResults'] = maxResults
        if properties is not None:
            _body['properties'] = properties
        if startAt is not None:
            _body['startAt'] = startAt
        if validateQuery is not None:
            _body['validateQuery'] = validateQuery
        rel_path = '/rest/api/3/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def count_issues(self, jql: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Count issues using JQL

HTTP POST /rest/api/3/search/approximate-count
Body (application/json) fields:
  - jql (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if jql is not None:
            _body['jql'] = jql
        rel_path = '/rest/api/3/search/approximate-count'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_and_reconsile_issues_using_jql(self, jql: Optional[str]=None, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, fields: Optional[list[str]]=None, expand: Optional[str]=None, properties: Optional[list[str]]=None, fieldsByKeys: Optional[bool]=None, failFast: Optional[bool]=None, reconcileIssues: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search for issues using JQL enhanced search (GET)

HTTP GET /rest/api/3/search/jql
Query params:
  - jql (str, optional)
  - nextPageToken (str, optional)
  - maxResults (int, optional)
  - fields (list[str], optional)
  - expand (str, optional)
  - properties (list[str], optional)
  - fieldsByKeys (bool, optional)
  - failFast (bool, optional)
  - reconcileIssues (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if jql is not None:
            _query['jql'] = jql
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if fields is not None:
            _query['fields'] = fields
        if expand is not None:
            _query['expand'] = expand
        if properties is not None:
            _query['properties'] = properties
        if fieldsByKeys is not None:
            _query['fieldsByKeys'] = fieldsByKeys
        if failFast is not None:
            _query['failFast'] = failFast
        if reconcileIssues is not None:
            _query['reconcileIssues'] = reconcileIssues
        _body = None
        rel_path = '/rest/api/3/search/jql'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_and_reconsile_issues_using_jql_post(self, expand: Optional[str]=None, fields: Optional[list[str]]=None, fieldsByKeys: Optional[bool]=None, jql: Optional[str]=None, maxResults: Optional[int]=None, nextPageToken: Optional[str]=None, properties: Optional[list[str]]=None, reconcileIssues: Optional[list[int]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search for issues using JQL enhanced search (POST)

HTTP POST /rest/api/3/search/jql
Body (application/json) fields:
  - expand (str, optional)
  - fields (list[str], optional)
  - fieldsByKeys (bool, optional)
  - jql (str, optional)
  - maxResults (int, optional)
  - nextPageToken (str, optional)
  - properties (list[str], optional)
  - reconcileIssues (list[int], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if expand is not None:
            _body['expand'] = expand
        if fields is not None:
            _body['fields'] = fields
        if fieldsByKeys is not None:
            _body['fieldsByKeys'] = fieldsByKeys
        if jql is not None:
            _body['jql'] = jql
        if maxResults is not None:
            _body['maxResults'] = maxResults
        if nextPageToken is not None:
            _body['nextPageToken'] = nextPageToken
        if properties is not None:
            _body['properties'] = properties
        if reconcileIssues is not None:
            _body['reconcileIssues'] = reconcileIssues
        rel_path = '/rest/api/3/search/jql'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_security_level(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue security level

HTTP GET /rest/api/3/securitylevel/{id}
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/securitylevel/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_server_info(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get Jira instance info

HTTP GET /rest/api/3/serverInfo"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/serverInfo'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_issue_navigator_default_columns(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue navigator default columns

HTTP GET /rest/api/3/settings/columns"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/settings/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_issue_navigator_default_columns(self, columns: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set issue navigator default columns

HTTP PUT /rest/api/3/settings/columns
Body (multipart/form-data) fields:
  - columns (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'multipart/form-data')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if columns is not None:
            _body['columns'] = columns
        rel_path = '/rest/api/3/settings/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_statuses(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all statuses

HTTP GET /rest/api/3/status"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/status'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_status(self, idOrName: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get status

HTTP GET /rest/api/3/status/{idOrName}
Path params:
  - idOrName (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'idOrName': idOrName}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/status/{idOrName}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_status_categories(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all status categories

HTTP GET /rest/api/3/statuscategory"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/statuscategory'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_status_category(self, idOrKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get status category

HTTP GET /rest/api/3/statuscategory/{idOrKey}
Path params:
  - idOrKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'idOrKey': idOrKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/statuscategory/{idOrKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_statuses_by_id(self, id: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk delete Statuses

HTTP DELETE /rest/api/3/statuses
Query params:
  - id (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['id'] = id
        _body = None
        rel_path = '/rest/api/3/statuses'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_statuses_by_id(self, id: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk get statuses

HTTP GET /rest/api/3/statuses
Query params:
  - id (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['id'] = id
        _body = None
        rel_path = '/rest/api/3/statuses'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_statuses(self, scope: Dict[str, Any], statuses: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk create statuses

HTTP POST /rest/api/3/statuses
Body (application/json) fields:
  - scope (Dict[str, Any], required)
  - statuses (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['scope'] = scope
        _body['statuses'] = statuses
        rel_path = '/rest/api/3/statuses'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_statuses(self, statuses: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk update statuses

HTTP PUT /rest/api/3/statuses
Body (application/json) fields:
  - statuses (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['statuses'] = statuses
        rel_path = '/rest/api/3/statuses'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search(self, projectId: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, searchString: Optional[str]=None, statusCategory: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search statuses paginated

HTTP GET /rest/api/3/statuses/search
Query params:
  - projectId (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - searchString (str, optional)
  - statusCategory (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if projectId is not None:
            _query['projectId'] = projectId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if searchString is not None:
            _query['searchString'] = searchString
        if statusCategory is not None:
            _query['statusCategory'] = statusCategory
        _body = None
        rel_path = '/rest/api/3/statuses/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_issue_type_usages_for_status(self, statusId: str, projectId: str, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue type usages by status and project

HTTP GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages
Path params:
  - statusId (str)
  - projectId (str)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'statusId': statusId, 'projectId': projectId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_usages_for_status(self, statusId: str, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get project usages by status

HTTP GET /rest/api/3/statuses/{statusId}/projectUsages
Path params:
  - statusId (str)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'statusId': statusId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/statuses/{statusId}/projectUsages'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_usages_for_status(self, statusId: str, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow usages by status

HTTP GET /rest/api/3/statuses/{statusId}/workflowUsages
Path params:
  - statusId (str)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'statusId': statusId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/statuses/{statusId}/workflowUsages'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_task(self, taskId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get task

HTTP GET /rest/api/3/task/{taskId}
Path params:
  - taskId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'taskId': taskId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/task/{taskId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def cancel_task(self, taskId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Cancel task

HTTP POST /rest/api/3/task/{taskId}/cancel
Path params:
  - taskId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'taskId': taskId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/task/{taskId}/cancel'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_ui_modifications(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get UI modifications

HTTP GET /rest/api/3/uiModifications
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/uiModifications'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_ui_modification(self, name: str, contexts: Optional[list[Dict[str, Any]]]=None, data: Optional[str]=None, description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create UI modification

HTTP POST /rest/api/3/uiModifications
Body (application/json) fields:
  - contexts (list[Dict[str, Any]], optional)
  - data (str, optional)
  - description (str, optional)
  - name (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if contexts is not None:
            _body['contexts'] = contexts
        if data is not None:
            _body['data'] = data
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        rel_path = '/rest/api/3/uiModifications'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_ui_modification(self, uiModificationId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete UI modification

HTTP DELETE /rest/api/3/uiModifications/{uiModificationId}
Path params:
  - uiModificationId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'uiModificationId': uiModificationId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/uiModifications/{uiModificationId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_ui_modification(self, uiModificationId: str, contexts: Optional[list[Dict[str, Any]]]=None, data: Optional[str]=None, description: Optional[str]=None, name: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update UI modification

HTTP PUT /rest/api/3/uiModifications/{uiModificationId}
Path params:
  - uiModificationId (str)
Body (application/json) fields:
  - contexts (list[Dict[str, Any]], optional)
  - data (str, optional)
  - description (str, optional)
  - name (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'uiModificationId': uiModificationId}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if contexts is not None:
            _body['contexts'] = contexts
        if data is not None:
            _body['data'] = data
        if description is not None:
            _body['description'] = description
        if name is not None:
            _body['name'] = name
        rel_path = '/rest/api/3/uiModifications/{uiModificationId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_avatars(self, type: str, entityId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get avatars

HTTP GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId}
Path params:
  - type (str)
  - entityId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'type': type, 'entityId': entityId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/universal_avatar/type/{type}/owner/{entityId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def store_avatar(self, type: str, entityId: str, size: int, x: Optional[int]=None, y: Optional[int]=None, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Load avatar

HTTP POST /rest/api/3/universal_avatar/type/{type}/owner/{entityId}
Path params:
  - type (str)
  - entityId (str)
Query params:
  - x (int, optional)
  - y (int, optional)
  - size (int, required)
Body: */* (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', '*/*')
        _path: Dict[str, Any] = {'type': type, 'entityId': entityId}
        _query: Dict[str, Any] = {}
        if x is not None:
            _query['x'] = x
        if y is not None:
            _query['y'] = y
        _query['size'] = size
        _body = body
        rel_path = '/rest/api/3/universal_avatar/type/{type}/owner/{entityId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_avatar(self, type: str, owningObjectId: str, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete avatar

HTTP DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}
Path params:
  - type (str)
  - owningObjectId (str)
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'type': type, 'owningObjectId': owningObjectId, 'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_avatar_image_by_type(self, type: str, size: Optional[str]=None, format: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get avatar image by type

HTTP GET /rest/api/3/universal_avatar/view/type/{type}
Path params:
  - type (str)
Query params:
  - size (str, optional)
  - format (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'type': type}
        _query: Dict[str, Any] = {}
        if size is not None:
            _query['size'] = size
        if format is not None:
            _query['format'] = format
        _body = None
        rel_path = '/rest/api/3/universal_avatar/view/type/{type}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_avatar_image_by_id(self, type: str, id: int, size: Optional[str]=None, format: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get avatar image by ID

HTTP GET /rest/api/3/universal_avatar/view/type/{type}/avatar/{id}
Path params:
  - type (str)
  - id (int)
Query params:
  - size (str, optional)
  - format (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'type': type, 'id': id}
        _query: Dict[str, Any] = {}
        if size is not None:
            _query['size'] = size
        if format is not None:
            _query['format'] = format
        _body = None
        rel_path = '/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_avatar_image_by_owner(self, type: str, entityId: str, size: Optional[str]=None, format: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get avatar image by owner

HTTP GET /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}
Path params:
  - type (str)
  - entityId (str)
Query params:
  - size (str, optional)
  - format (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'type': type, 'entityId': entityId}
        _query: Dict[str, Any] = {}
        if size is not None:
            _query['size'] = size
        if format is not None:
            _query['format'] = format
        _body = None
        rel_path = '/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def remove_user(self, accountId: str, username: Optional[str]=None, key: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete user

HTTP DELETE /rest/api/3/user
Query params:
  - accountId (str, required)
  - username (str, optional)
  - key (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['accountId'] = accountId
        if username is not None:
            _query['username'] = username
        if key is not None:
            _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/user'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user(self, accountId: Optional[str]=None, username: Optional[str]=None, key: Optional[str]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user

HTTP GET /rest/api/3/user
Query params:
  - accountId (str, optional)
  - username (str, optional)
  - key (str, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if username is not None:
            _query['username'] = username
        if key is not None:
            _query['key'] = key
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/user'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_user(self, emailAddress: str, products: list[str], applicationKeys: Optional[list[str]]=None, displayName: Optional[str]=None, key: Optional[str]=None, name: Optional[str]=None, password: Optional[str]=None, self_: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create user

HTTP POST /rest/api/3/user
Body (application/json) fields:
  - applicationKeys (list[str], optional)
  - displayName (str, optional)
  - emailAddress (str, required)
  - key (str, optional)
  - name (str, optional)
  - password (str, optional)
  - products (list[str], required)
  - self (str, optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if applicationKeys is not None:
            _body['applicationKeys'] = applicationKeys
        if displayName is not None:
            _body['displayName'] = displayName
        _body['emailAddress'] = emailAddress
        if key is not None:
            _body['key'] = key
        if name is not None:
            _body['name'] = name
        if password is not None:
            _body['password'] = password
        _body['products'] = products
        if self_ is not None:
            _body['self'] = self_
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/user'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_bulk_assignable_users(self, projectKeys: str, query: Optional[str]=None, username: Optional[str]=None, accountId: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users assignable to projects

HTTP GET /rest/api/3/user/assignable/multiProjectSearch
Query params:
  - query (str, optional)
  - username (str, optional)
  - accountId (str, optional)
  - projectKeys (str, required)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if query is not None:
            _query['query'] = query
        if username is not None:
            _query['username'] = username
        if accountId is not None:
            _query['accountId'] = accountId
        _query['projectKeys'] = projectKeys
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/user/assignable/multiProjectSearch'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_assignable_users(self, query: Optional[str]=None, sessionId: Optional[str]=None, username: Optional[str]=None, accountId: Optional[str]=None, project: Optional[str]=None, issueKey: Optional[str]=None, issueId: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, actionDescriptorId: Optional[int]=None, recommend: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users assignable to issues

HTTP GET /rest/api/3/user/assignable/search
Query params:
  - query (str, optional)
  - sessionId (str, optional)
  - username (str, optional)
  - accountId (str, optional)
  - project (str, optional)
  - issueKey (str, optional)
  - issueId (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - actionDescriptorId (int, optional)
  - recommend (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if query is not None:
            _query['query'] = query
        if sessionId is not None:
            _query['sessionId'] = sessionId
        if username is not None:
            _query['username'] = username
        if accountId is not None:
            _query['accountId'] = accountId
        if project is not None:
            _query['project'] = project
        if issueKey is not None:
            _query['issueKey'] = issueKey
        if issueId is not None:
            _query['issueId'] = issueId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if actionDescriptorId is not None:
            _query['actionDescriptorId'] = actionDescriptorId
        if recommend is not None:
            _query['recommend'] = recommend
        _body = None
        rel_path = '/rest/api/3/user/assignable/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_get_users(self, accountId: list[str], startAt: Optional[int]=None, maxResults: Optional[int]=None, username: Optional[list[str]]=None, key: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk get users

HTTP GET /rest/api/3/user/bulk
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - username (list[str], optional)
  - key (list[str], optional)
  - accountId (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if username is not None:
            _query['username'] = username
        if key is not None:
            _query['key'] = key
        _query['accountId'] = accountId
        _body = None
        rel_path = '/rest/api/3/user/bulk'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def bulk_get_users_migration(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, username: Optional[list[str]]=None, key: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get account IDs for users

HTTP GET /rest/api/3/user/bulk/migration
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - username (list[str], optional)
  - key (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if username is not None:
            _query['username'] = username
        if key is not None:
            _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/user/bulk/migration'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def reset_user_columns(self, accountId: Optional[str]=None, username: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Reset user default columns

HTTP DELETE /rest/api/3/user/columns
Query params:
  - accountId (str, optional)
  - username (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if username is not None:
            _query['username'] = username
        _body = None
        rel_path = '/rest/api/3/user/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_default_columns(self, accountId: Optional[str]=None, username: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user default columns

HTTP GET /rest/api/3/user/columns
Query params:
  - accountId (str, optional)
  - username (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if username is not None:
            _query['username'] = username
        _body = None
        rel_path = '/rest/api/3/user/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_user_columns(self, accountId: Optional[str]=None, columns: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set user default columns

HTTP PUT /rest/api/3/user/columns
Query params:
  - accountId (str, optional)
Body (multipart/form-data) fields:
  - columns (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'multipart/form-data')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        _body: Dict[str, Any] = {}
        if columns is not None:
            _body['columns'] = columns
        rel_path = '/rest/api/3/user/columns'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_email(self, accountId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user email

HTTP GET /rest/api/3/user/email
Query params:
  - accountId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['accountId'] = accountId
        _body = None
        rel_path = '/rest/api/3/user/email'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_email_bulk(self, accountId: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user email bulk

HTTP GET /rest/api/3/user/email/bulk
Query params:
  - accountId (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['accountId'] = accountId
        _body = None
        rel_path = '/rest/api/3/user/email/bulk'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_groups(self, accountId: str, username: Optional[str]=None, key: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user groups

HTTP GET /rest/api/3/user/groups
Query params:
  - accountId (str, required)
  - username (str, optional)
  - key (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['accountId'] = accountId
        if username is not None:
            _query['username'] = username
        if key is not None:
            _query['key'] = key
        _body = None
        rel_path = '/rest/api/3/user/groups'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_nav_property(self, propertyKey: str, accountId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user nav property

HTTP GET /rest/api/3/user/nav4-opt-property/{propertyKey}
Path params:
  - propertyKey (str)
Query params:
  - accountId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        _body = None
        rel_path = '/rest/api/3/user/nav4-opt-property/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_user_nav_property(self, propertyKey: str, accountId: Optional[str]=None, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set user nav property

HTTP PUT /rest/api/3/user/nav4-opt-property/{propertyKey}
Path params:
  - propertyKey (str)
Query params:
  - accountId (str, optional)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        _body = body
        rel_path = '/rest/api/3/user/nav4-opt-property/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_users_with_all_permissions(self, permissions: str, query: Optional[str]=None, username: Optional[str]=None, accountId: Optional[str]=None, issueKey: Optional[str]=None, projectKey: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users with permissions

HTTP GET /rest/api/3/user/permission/search
Query params:
  - query (str, optional)
  - username (str, optional)
  - accountId (str, optional)
  - permissions (str, required)
  - issueKey (str, optional)
  - projectKey (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if query is not None:
            _query['query'] = query
        if username is not None:
            _query['username'] = username
        if accountId is not None:
            _query['accountId'] = accountId
        _query['permissions'] = permissions
        if issueKey is not None:
            _query['issueKey'] = issueKey
        if projectKey is not None:
            _query['projectKey'] = projectKey
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/user/permission/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_users_for_picker(self, query: str, maxResults: Optional[int]=None, showAvatar: Optional[bool]=None, exclude: Optional[list[str]]=None, excludeAccountIds: Optional[list[str]]=None, avatarSize: Optional[str]=None, excludeConnectUsers: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users for picker

HTTP GET /rest/api/3/user/picker
Query params:
  - query (str, required)
  - maxResults (int, optional)
  - showAvatar (bool, optional)
  - exclude (list[str], optional)
  - excludeAccountIds (list[str], optional)
  - avatarSize (str, optional)
  - excludeConnectUsers (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['query'] = query
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if showAvatar is not None:
            _query['showAvatar'] = showAvatar
        if exclude is not None:
            _query['exclude'] = exclude
        if excludeAccountIds is not None:
            _query['excludeAccountIds'] = excludeAccountIds
        if avatarSize is not None:
            _query['avatarSize'] = avatarSize
        if excludeConnectUsers is not None:
            _query['excludeConnectUsers'] = excludeConnectUsers
        _body = None
        rel_path = '/rest/api/3/user/picker'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_property_keys(self, accountId: Optional[str]=None, userKey: Optional[str]=None, username: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user property keys

HTTP GET /rest/api/3/user/properties
Query params:
  - accountId (str, optional)
  - userKey (str, optional)
  - username (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if userKey is not None:
            _query['userKey'] = userKey
        if username is not None:
            _query['username'] = username
        _body = None
        rel_path = '/rest/api/3/user/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_user_property(self, propertyKey: str, accountId: Optional[str]=None, userKey: Optional[str]=None, username: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete user property

HTTP DELETE /rest/api/3/user/properties/{propertyKey}
Path params:
  - propertyKey (str)
Query params:
  - accountId (str, optional)
  - userKey (str, optional)
  - username (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if userKey is not None:
            _query['userKey'] = userKey
        if username is not None:
            _query['username'] = username
        _body = None
        rel_path = '/rest/api/3/user/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_user_property(self, propertyKey: str, accountId: Optional[str]=None, userKey: Optional[str]=None, username: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get user property

HTTP GET /rest/api/3/user/properties/{propertyKey}
Path params:
  - propertyKey (str)
Query params:
  - accountId (str, optional)
  - userKey (str, optional)
  - username (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if userKey is not None:
            _query['userKey'] = userKey
        if username is not None:
            _query['username'] = username
        _body = None
        rel_path = '/rest/api/3/user/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_user_property(self, propertyKey: str, accountId: Optional[str]=None, userKey: Optional[str]=None, username: Optional[str]=None, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set user property

HTTP PUT /rest/api/3/user/properties/{propertyKey}
Path params:
  - propertyKey (str)
Query params:
  - accountId (str, optional)
  - userKey (str, optional)
  - username (str, optional)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        if accountId is not None:
            _query['accountId'] = accountId
        if userKey is not None:
            _query['userKey'] = userKey
        if username is not None:
            _query['username'] = username
        _body = body
        rel_path = '/rest/api/3/user/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_users(self, query: Optional[str]=None, username: Optional[str]=None, accountId: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, property: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users

HTTP GET /rest/api/3/user/search
Query params:
  - query (str, optional)
  - username (str, optional)
  - accountId (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)
  - property (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if query is not None:
            _query['query'] = query
        if username is not None:
            _query['username'] = username
        if accountId is not None:
            _query['accountId'] = accountId
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if property is not None:
            _query['property'] = property
        _body = None
        rel_path = '/rest/api/3/user/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_users_by_query(self, query: str, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users by query

HTTP GET /rest/api/3/user/search/query
Query params:
  - query (str, required)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['query'] = query
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/user/search/query'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_user_keys_by_query(self, query: str, startAt: Optional[int]=None, maxResult: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find user keys by query

HTTP GET /rest/api/3/user/search/query/key
Query params:
  - query (str, required)
  - startAt (int, optional)
  - maxResult (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['query'] = query
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResult is not None:
            _query['maxResult'] = maxResult
        _body = None
        rel_path = '/rest/api/3/user/search/query/key'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def find_users_with_browse_permission(self, query: Optional[str]=None, username: Optional[str]=None, accountId: Optional[str]=None, issueKey: Optional[str]=None, projectKey: Optional[str]=None, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Find users with browse permission

HTTP GET /rest/api/3/user/viewissue/search
Query params:
  - query (str, optional)
  - username (str, optional)
  - accountId (str, optional)
  - issueKey (str, optional)
  - projectKey (str, optional)
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if query is not None:
            _query['query'] = query
        if username is not None:
            _query['username'] = username
        if accountId is not None:
            _query['accountId'] = accountId
        if issueKey is not None:
            _query['issueKey'] = issueKey
        if projectKey is not None:
            _query['projectKey'] = projectKey
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/user/viewissue/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_users_default(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all users default

HTTP GET /rest/api/3/users
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/users'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_users(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all users

HTTP GET /rest/api/3/users/search
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/users/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_version(self, approvers: Optional[list[Dict[str, Any]]]=None, archived: Optional[bool]=None, description: Optional[str]=None, driver: Optional[str]=None, expand: Optional[str]=None, id: Optional[str]=None, issuesStatusForFixVersion: Optional[Dict[str, Any]]=None, moveUnfixedIssuesTo: Optional[str]=None, name: Optional[str]=None, operations: Optional[list[Dict[str, Any]]]=None, overdue: Optional[bool]=None, project: Optional[str]=None, projectId: Optional[int]=None, releaseDate: Optional[str]=None, released: Optional[bool]=None, self_: Optional[str]=None, startDate: Optional[str]=None, userReleaseDate: Optional[str]=None, userStartDate: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create version

HTTP POST /rest/api/3/version
Body (application/json) fields:
  - approvers (list[Dict[str, Any]], optional)
  - archived (bool, optional)
  - description (str, optional)
  - driver (str, optional)
  - expand (str, optional)
  - id (str, optional)
  - issuesStatusForFixVersion (Dict[str, Any], optional)
  - moveUnfixedIssuesTo (str, optional)
  - name (str, optional)
  - operations (list[Dict[str, Any]], optional)
  - overdue (bool, optional)
  - project (str, optional)
  - projectId (int, optional)
  - releaseDate (str, optional)
  - released (bool, optional)
  - self (str, optional)
  - startDate (str, optional)
  - userReleaseDate (str, optional)
  - userStartDate (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if approvers is not None:
            _body['approvers'] = approvers
        if archived is not None:
            _body['archived'] = archived
        if description is not None:
            _body['description'] = description
        if driver is not None:
            _body['driver'] = driver
        if expand is not None:
            _body['expand'] = expand
        if id is not None:
            _body['id'] = id
        if issuesStatusForFixVersion is not None:
            _body['issuesStatusForFixVersion'] = issuesStatusForFixVersion
        if moveUnfixedIssuesTo is not None:
            _body['moveUnfixedIssuesTo'] = moveUnfixedIssuesTo
        if name is not None:
            _body['name'] = name
        if operations is not None:
            _body['operations'] = operations
        if overdue is not None:
            _body['overdue'] = overdue
        if project is not None:
            _body['project'] = project
        if projectId is not None:
            _body['projectId'] = projectId
        if releaseDate is not None:
            _body['releaseDate'] = releaseDate
        if released is not None:
            _body['released'] = released
        if self_ is not None:
            _body['self'] = self_
        if startDate is not None:
            _body['startDate'] = startDate
        if userReleaseDate is not None:
            _body['userReleaseDate'] = userReleaseDate
        if userStartDate is not None:
            _body['userStartDate'] = userStartDate
        rel_path = '/rest/api/3/version'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_version(self, id: str, moveFixIssuesTo: Optional[str]=None, moveAffectedIssuesTo: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete version

HTTP DELETE /rest/api/3/version/{id}
Path params:
  - id (str)
Query params:
  - moveFixIssuesTo (str, optional)
  - moveAffectedIssuesTo (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if moveFixIssuesTo is not None:
            _query['moveFixIssuesTo'] = moveFixIssuesTo
        if moveAffectedIssuesTo is not None:
            _query['moveAffectedIssuesTo'] = moveAffectedIssuesTo
        _body = None
        rel_path = '/rest/api/3/version/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_version(self, id: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get version

HTTP GET /rest/api/3/version/{id}
Path params:
  - id (str)
Query params:
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/version/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_version(self, id: str, approvers: Optional[list[Dict[str, Any]]]=None, archived: Optional[bool]=None, description: Optional[str]=None, driver: Optional[str]=None, expand: Optional[str]=None, id_body: Optional[str]=None, issuesStatusForFixVersion: Optional[Dict[str, Any]]=None, moveUnfixedIssuesTo: Optional[str]=None, name: Optional[str]=None, operations: Optional[list[Dict[str, Any]]]=None, overdue: Optional[bool]=None, project: Optional[str]=None, projectId: Optional[int]=None, releaseDate: Optional[str]=None, released: Optional[bool]=None, self_: Optional[str]=None, startDate: Optional[str]=None, userReleaseDate: Optional[str]=None, userStartDate: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update version

HTTP PUT /rest/api/3/version/{id}
Path params:
  - id (str)
Body (application/json) fields:
  - approvers (list[Dict[str, Any]], optional)
  - archived (bool, optional)
  - description (str, optional)
  - driver (str, optional)
  - expand (str, optional)
  - id (str, optional)
  - issuesStatusForFixVersion (Dict[str, Any], optional)
  - moveUnfixedIssuesTo (str, optional)
  - name (str, optional)
  - operations (list[Dict[str, Any]], optional)
  - overdue (bool, optional)
  - project (str, optional)
  - projectId (int, optional)
  - releaseDate (str, optional)
  - released (bool, optional)
  - self (str, optional)
  - startDate (str, optional)
  - userReleaseDate (str, optional)
  - userStartDate (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if approvers is not None:
            _body['approvers'] = approvers
        if archived is not None:
            _body['archived'] = archived
        if description is not None:
            _body['description'] = description
        if driver is not None:
            _body['driver'] = driver
        if expand is not None:
            _body['expand'] = expand
        if id_body is not None:
            _body['id'] = id_body
        if issuesStatusForFixVersion is not None:
            _body['issuesStatusForFixVersion'] = issuesStatusForFixVersion
        if moveUnfixedIssuesTo is not None:
            _body['moveUnfixedIssuesTo'] = moveUnfixedIssuesTo
        if name is not None:
            _body['name'] = name
        if operations is not None:
            _body['operations'] = operations
        if overdue is not None:
            _body['overdue'] = overdue
        if project is not None:
            _body['project'] = project
        if projectId is not None:
            _body['projectId'] = projectId
        if releaseDate is not None:
            _body['releaseDate'] = releaseDate
        if released is not None:
            _body['released'] = released
        if self_ is not None:
            _body['self'] = self_
        if startDate is not None:
            _body['startDate'] = startDate
        if userReleaseDate is not None:
            _body['userReleaseDate'] = userReleaseDate
        if userStartDate is not None:
            _body['userStartDate'] = userStartDate
        rel_path = '/rest/api/3/version/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def merge_versions(self, id: str, moveIssuesTo: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Merge versions

HTTP PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}
Path params:
  - id (str)
  - moveIssuesTo (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'moveIssuesTo': moveIssuesTo}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/version/{id}/mergeto/{moveIssuesTo}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def move_version(self, id: str, after: Optional[str]=None, position: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Move version

HTTP POST /rest/api/3/version/{id}/move
Path params:
  - id (str)
Body (application/json) fields:
  - after (str, optional)
  - position (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if after is not None:
            _body['after'] = after
        if position is not None:
            _body['position'] = position
        rel_path = '/rest/api/3/version/{id}/move'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_version_related_issues(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get version's related issues count

HTTP GET /rest/api/3/version/{id}/relatedIssueCounts
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/version/{id}/relatedIssueCounts'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_related_work(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get related work

HTTP GET /rest/api/3/version/{id}/relatedwork
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/version/{id}/relatedwork'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_related_work(self, id: str, category: str, issueId: Optional[int]=None, relatedWorkId: Optional[str]=None, title: Optional[str]=None, url: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create related work

HTTP POST /rest/api/3/version/{id}/relatedwork
Path params:
  - id (str)
Body (application/json) fields:
  - category (str, required)
  - issueId (int, optional)
  - relatedWorkId (str, optional)
  - title (str, optional)
  - url (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['category'] = category
        if issueId is not None:
            _body['issueId'] = issueId
        if relatedWorkId is not None:
            _body['relatedWorkId'] = relatedWorkId
        if title is not None:
            _body['title'] = title
        if url is not None:
            _body['url'] = url
        rel_path = '/rest/api/3/version/{id}/relatedwork'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_related_work(self, id: str, category: str, issueId: Optional[int]=None, relatedWorkId: Optional[str]=None, title: Optional[str]=None, url: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update related work

HTTP PUT /rest/api/3/version/{id}/relatedwork
Path params:
  - id (str)
Body (application/json) fields:
  - category (str, required)
  - issueId (int, optional)
  - relatedWorkId (str, optional)
  - title (str, optional)
  - url (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['category'] = category
        if issueId is not None:
            _body['issueId'] = issueId
        if relatedWorkId is not None:
            _body['relatedWorkId'] = relatedWorkId
        if title is not None:
            _body['title'] = title
        if url is not None:
            _body['url'] = url
        rel_path = '/rest/api/3/version/{id}/relatedwork'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_and_replace_version(self, id: str, customFieldReplacementList: Optional[list[Dict[str, Any]]]=None, moveAffectedIssuesTo: Optional[int]=None, moveFixIssuesTo: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete and replace version

HTTP POST /rest/api/3/version/{id}/removeAndSwap
Path params:
  - id (str)
Body (application/json) fields:
  - customFieldReplacementList (list[Dict[str, Any]], optional)
  - moveAffectedIssuesTo (int, optional)
  - moveFixIssuesTo (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if customFieldReplacementList is not None:
            _body['customFieldReplacementList'] = customFieldReplacementList
        if moveAffectedIssuesTo is not None:
            _body['moveAffectedIssuesTo'] = moveAffectedIssuesTo
        if moveFixIssuesTo is not None:
            _body['moveFixIssuesTo'] = moveFixIssuesTo
        rel_path = '/rest/api/3/version/{id}/removeAndSwap'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_version_unresolved_issues(self, id: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get version's unresolved issues count

HTTP GET /rest/api/3/version/{id}/unresolvedIssueCount
Path params:
  - id (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/version/{id}/unresolvedIssueCount'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_related_work(self, versionId: str, relatedWorkId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete related work

HTTP DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}
Path params:
  - versionId (str)
  - relatedWorkId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'versionId': versionId, 'relatedWorkId': relatedWorkId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_webhook_by_id(self, webhookIds: list[int], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete webhooks by ID

HTTP DELETE /rest/api/3/webhook
Body (application/json) fields:
  - webhookIds (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['webhookIds'] = webhookIds
        rel_path = '/rest/api/3/webhook'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_dynamic_webhooks_for_app(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get dynamic webhooks for app

HTTP GET /rest/api/3/webhook
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/webhook'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def register_dynamic_webhooks(self, url: str, webhooks: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Register dynamic webhooks

HTTP POST /rest/api/3/webhook
Body (application/json) fields:
  - url (str, required)
  - webhooks (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['url'] = url
        _body['webhooks'] = webhooks
        rel_path = '/rest/api/3/webhook'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_failed_webhooks(self, maxResults: Optional[int]=None, after: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get failed webhooks

HTTP GET /rest/api/3/webhook/failed
Query params:
  - maxResults (int, optional)
  - after (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if after is not None:
            _query['after'] = after
        _body = None
        rel_path = '/rest/api/3/webhook/failed'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def refresh_webhooks(self, webhookIds: list[int], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Extend webhook life

HTTP PUT /rest/api/3/webhook/refresh
Body (application/json) fields:
  - webhookIds (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['webhookIds'] = webhookIds
        rel_path = '/rest/api/3/webhook/refresh'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_workflows(self, workflowName: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all workflows

HTTP GET /rest/api/3/workflow
Query params:
  - workflowName (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if workflowName is not None:
            _query['workflowName'] = workflowName
        _body = None
        rel_path = '/rest/api/3/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_workflow(self, name: str, statuses: list[Dict[str, Any]], transitions: list[Dict[str, Any]], description: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create workflow

HTTP POST /rest/api/3/workflow
Body (application/json) fields:
  - description (str, optional)
  - name (str, required)
  - statuses (list[Dict[str, Any]], required)
  - transitions (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if description is not None:
            _body['description'] = description
        _body['name'] = name
        _body['statuses'] = statuses
        _body['transitions'] = transitions
        rel_path = '/rest/api/3/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_transition_rule_configurations(self, types: list[str], startAt: Optional[int]=None, maxResults: Optional[int]=None, keys: Optional[list[str]]=None, workflowNames: Optional[list[str]]=None, withTags: Optional[list[str]]=None, draft: Optional[bool]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow transition rule configurations

HTTP GET /rest/api/3/workflow/rule/config
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - types (list[str], required)
  - keys (list[str], optional)
  - workflowNames (list[str], optional)
  - withTags (list[str], optional)
  - draft (bool, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _query['types'] = types
        if keys is not None:
            _query['keys'] = keys
        if workflowNames is not None:
            _query['workflowNames'] = workflowNames
        if withTags is not None:
            _query['withTags'] = withTags
        if draft is not None:
            _query['draft'] = draft
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/workflow/rule/config'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflow_transition_rule_configurations(self, workflows: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update workflow transition rule configurations

HTTP PUT /rest/api/3/workflow/rule/config
Body (application/json) fields:
  - workflows (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['workflows'] = workflows
        rel_path = '/rest/api/3/workflow/rule/config'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_transition_rule_configurations(self, workflows: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete workflow transition rule configurations

HTTP PUT /rest/api/3/workflow/rule/config/delete
Body (application/json) fields:
  - workflows (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['workflows'] = workflows
        rel_path = '/rest/api/3/workflow/rule/config/delete'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflows_paginated(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, workflowName: Optional[list[str]]=None, expand: Optional[str]=None, queryString: Optional[str]=None, orderBy: Optional[str]=None, isActive: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflows paginated

HTTP GET /rest/api/3/workflow/search
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - workflowName (list[str], optional)
  - expand (str, optional)
  - queryString (str, optional)
  - orderBy (str, optional)
  - isActive (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if workflowName is not None:
            _query['workflowName'] = workflowName
        if expand is not None:
            _query['expand'] = expand
        if queryString is not None:
            _query['queryString'] = queryString
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if isActive is not None:
            _query['isActive'] = isActive
        _body = None
        rel_path = '/rest/api/3/workflow/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_transition_property(self, transitionId: int, key: str, workflowName: str, workflowMode: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete workflow transition property

HTTP DELETE /rest/api/3/workflow/transitions/{transitionId}/properties
Path params:
  - transitionId (int)
Query params:
  - key (str, required)
  - workflowName (str, required)
  - workflowMode (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'transitionId': transitionId}
        _query: Dict[str, Any] = {}
        _query['key'] = key
        _query['workflowName'] = workflowName
        if workflowMode is not None:
            _query['workflowMode'] = workflowMode
        _body = None
        rel_path = '/rest/api/3/workflow/transitions/{transitionId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_transition_properties(self, transitionId: int, workflowName: str, includeReservedKeys: Optional[bool]=None, key: Optional[str]=None, workflowMode: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow transition properties

HTTP GET /rest/api/3/workflow/transitions/{transitionId}/properties
Path params:
  - transitionId (int)
Query params:
  - includeReservedKeys (bool, optional)
  - key (str, optional)
  - workflowName (str, required)
  - workflowMode (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'transitionId': transitionId}
        _query: Dict[str, Any] = {}
        if includeReservedKeys is not None:
            _query['includeReservedKeys'] = includeReservedKeys
        if key is not None:
            _query['key'] = key
        _query['workflowName'] = workflowName
        if workflowMode is not None:
            _query['workflowMode'] = workflowMode
        _body = None
        rel_path = '/rest/api/3/workflow/transitions/{transitionId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_workflow_transition_property(self, transitionId: int, key: str, workflowName: str, value: str, workflowMode: Optional[str]=None, id: Optional[str]=None, key_body: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create workflow transition property

HTTP POST /rest/api/3/workflow/transitions/{transitionId}/properties
Path params:
  - transitionId (int)
Query params:
  - key (str, required)
  - workflowName (str, required)
  - workflowMode (str, optional)
Body (application/json) fields:
  - id (str, optional)
  - key (str, optional)
  - value (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'transitionId': transitionId}
        _query: Dict[str, Any] = {}
        _query['key'] = key
        _query['workflowName'] = workflowName
        if workflowMode is not None:
            _query['workflowMode'] = workflowMode
        _body: Dict[str, Any] = {}
        if id is not None:
            _body['id'] = id
        if key_body is not None:
            _body['key'] = key_body
        _body['value'] = value
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/workflow/transitions/{transitionId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflow_transition_property(self, transitionId: int, key: str, workflowName: str, value: str, workflowMode: Optional[str]=None, id: Optional[str]=None, key_body: Optional[str]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update workflow transition property

HTTP PUT /rest/api/3/workflow/transitions/{transitionId}/properties
Path params:
  - transitionId (int)
Query params:
  - key (str, required)
  - workflowName (str, required)
  - workflowMode (str, optional)
Body (application/json) fields:
  - id (str, optional)
  - key (str, optional)
  - value (str, required)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'transitionId': transitionId}
        _query: Dict[str, Any] = {}
        _query['key'] = key
        _query['workflowName'] = workflowName
        if workflowMode is not None:
            _query['workflowMode'] = workflowMode
        _body: Dict[str, Any] = {}
        if id is not None:
            _body['id'] = id
        if key_body is not None:
            _body['key'] = key_body
        _body['value'] = value
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/workflow/transitions/{transitionId}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_inactive_workflow(self, entityId: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete inactive workflow

HTTP DELETE /rest/api/3/workflow/{entityId}
Path params:
  - entityId (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'entityId': entityId}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflow/{entityId}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_project_issue_type_usages(self, workflowId: str, projectId: int, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue types in a project that are using a given workflow

HTTP GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages
Path params:
  - workflowId (str)
  - projectId (int)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'workflowId': workflowId, 'projectId': projectId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_usages_for_workflow(self, workflowId: str, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get projects using a given workflow

HTTP GET /rest/api/3/workflow/{workflowId}/projectUsages
Path params:
  - workflowId (str)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'workflowId': workflowId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/workflow/{workflowId}/projectUsages'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_scheme_usages_for_workflow(self, workflowId: str, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow schemes which are using a given workflow

HTTP GET /rest/api/3/workflow/{workflowId}/workflowSchemes
Path params:
  - workflowId (str)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'workflowId': workflowId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/workflow/{workflowId}/workflowSchemes'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def read_workflows(self, useApprovalConfiguration: Optional[bool]=None, projectAndIssueTypes: Optional[list[Dict[str, Any]]]=None, workflowIds: Optional[list[str]]=None, workflowNames: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk get workflows

HTTP POST /rest/api/3/workflows
Query params:
  - useApprovalConfiguration (bool, optional)
Body (application/json) fields:
  - projectAndIssueTypes (list[Dict[str, Any]], optional)
  - workflowIds (list[str], optional)
  - workflowNames (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if useApprovalConfiguration is not None:
            _query['useApprovalConfiguration'] = useApprovalConfiguration
        _body: Dict[str, Any] = {}
        if projectAndIssueTypes is not None:
            _body['projectAndIssueTypes'] = projectAndIssueTypes
        if workflowIds is not None:
            _body['workflowIds'] = workflowIds
        if workflowNames is not None:
            _body['workflowNames'] = workflowNames
        rel_path = '/rest/api/3/workflows'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def workflow_capabilities(self, workflowId: Optional[str]=None, projectId: Optional[str]=None, issueTypeId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get available workflow capabilities

HTTP GET /rest/api/3/workflows/capabilities
Query params:
  - workflowId (str, optional)
  - projectId (str, optional)
  - issueTypeId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if workflowId is not None:
            _query['workflowId'] = workflowId
        if projectId is not None:
            _query['projectId'] = projectId
        if issueTypeId is not None:
            _query['issueTypeId'] = issueTypeId
        _body = None
        rel_path = '/rest/api/3/workflows/capabilities'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_workflows(self, scope: Optional[Dict[str, Any]]=None, statuses: Optional[list[Dict[str, Any]]]=None, workflows: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk create workflows

HTTP POST /rest/api/3/workflows/create
Body (application/json) fields:
  - scope (Dict[str, Any], optional)
  - statuses (list[Dict[str, Any]], optional)
  - workflows (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if scope is not None:
            _body['scope'] = scope
        if statuses is not None:
            _body['statuses'] = statuses
        if workflows is not None:
            _body['workflows'] = workflows
        rel_path = '/rest/api/3/workflows/create'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def validate_create_workflows(self, payload: Dict[str, Any], validationOptions: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Validate create workflows

HTTP POST /rest/api/3/workflows/create/validation
Body (application/json) fields:
  - payload (Dict[str, Any], required)
  - validationOptions (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['payload'] = payload
        if validationOptions is not None:
            _body['validationOptions'] = validationOptions
        rel_path = '/rest/api/3/workflows/create/validation'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_default_editor(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get the user's default workflow editor

HTTP GET /rest/api/3/workflows/defaultEditor"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflows/defaultEditor'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def search_workflows(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, expand: Optional[str]=None, queryString: Optional[str]=None, orderBy: Optional[str]=None, scope: Optional[str]=None, isActive: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Search workflows

HTTP GET /rest/api/3/workflows/search
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)
  - expand (str, optional)
  - queryString (str, optional)
  - orderBy (str, optional)
  - scope (str, optional)
  - isActive (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        if expand is not None:
            _query['expand'] = expand
        if queryString is not None:
            _query['queryString'] = queryString
        if orderBy is not None:
            _query['orderBy'] = orderBy
        if scope is not None:
            _query['scope'] = scope
        if isActive is not None:
            _query['isActive'] = isActive
        _body = None
        rel_path = '/rest/api/3/workflows/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflows(self, statuses: Optional[list[Dict[str, Any]]]=None, workflows: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk update workflows

HTTP POST /rest/api/3/workflows/update
Body (application/json) fields:
  - statuses (list[Dict[str, Any]], optional)
  - workflows (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if statuses is not None:
            _body['statuses'] = statuses
        if workflows is not None:
            _body['workflows'] = workflows
        rel_path = '/rest/api/3/workflows/update'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def validate_update_workflows(self, payload: Dict[str, Any], validationOptions: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Validate update workflows

HTTP POST /rest/api/3/workflows/update/validation
Body (application/json) fields:
  - payload (Dict[str, Any], required)
  - validationOptions (Dict[str, Any], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['payload'] = payload
        if validationOptions is not None:
            _body['validationOptions'] = validationOptions
        rel_path = '/rest/api/3/workflows/update/validation'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_all_workflow_schemes(self, startAt: Optional[int]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get all workflow schemes

HTTP GET /rest/api/3/workflowscheme
Query params:
  - startAt (int, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if startAt is not None:
            _query['startAt'] = startAt
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/workflowscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_workflow_scheme(self, defaultWorkflow: Optional[str]=None, description: Optional[str]=None, draft: Optional[bool]=None, id: Optional[int]=None, issueTypeMappings: Optional[Dict[str, Any]]=None, issueTypes: Optional[Dict[str, Any]]=None, lastModified: Optional[str]=None, lastModifiedUser: Optional[Dict[str, Any]]=None, name: Optional[str]=None, originalDefaultWorkflow: Optional[str]=None, originalIssueTypeMappings: Optional[Dict[str, Any]]=None, self_: Optional[str]=None, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create workflow scheme

HTTP POST /rest/api/3/workflowscheme
Body (application/json) fields:
  - defaultWorkflow (str, optional)
  - description (str, optional)
  - draft (bool, optional)
  - id (int, optional)
  - issueTypeMappings (Dict[str, Any], optional)
  - issueTypes (Dict[str, Any], optional)
  - lastModified (str, optional)
  - lastModifiedUser (Dict[str, Any], optional)
  - name (str, optional)
  - originalDefaultWorkflow (str, optional)
  - originalIssueTypeMappings (Dict[str, Any], optional)
  - self (str, optional)
  - updateDraftIfNeeded (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultWorkflow is not None:
            _body['defaultWorkflow'] = defaultWorkflow
        if description is not None:
            _body['description'] = description
        if draft is not None:
            _body['draft'] = draft
        if id is not None:
            _body['id'] = id
        if issueTypeMappings is not None:
            _body['issueTypeMappings'] = issueTypeMappings
        if issueTypes is not None:
            _body['issueTypes'] = issueTypes
        if lastModified is not None:
            _body['lastModified'] = lastModified
        if lastModifiedUser is not None:
            _body['lastModifiedUser'] = lastModifiedUser
        if name is not None:
            _body['name'] = name
        if originalDefaultWorkflow is not None:
            _body['originalDefaultWorkflow'] = originalDefaultWorkflow
        if originalIssueTypeMappings is not None:
            _body['originalIssueTypeMappings'] = originalIssueTypeMappings
        if self_ is not None:
            _body['self'] = self_
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        rel_path = '/rest/api/3/workflowscheme'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_scheme_project_associations(self, projectId: list[int], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow scheme project associations

HTTP GET /rest/api/3/workflowscheme/project
Query params:
  - projectId (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['projectId'] = projectId
        _body = None
        rel_path = '/rest/api/3/workflowscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def assign_scheme_to_project(self, projectId: str, workflowSchemeId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Assign workflow scheme to project

HTTP PUT /rest/api/3/workflowscheme/project
Body (application/json) fields:
  - projectId (str, required)
  - workflowSchemeId (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['projectId'] = projectId
        if workflowSchemeId is not None:
            _body['workflowSchemeId'] = workflowSchemeId
        rel_path = '/rest/api/3/workflowscheme/project'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def read_workflow_schemes(self, projectIds: Optional[list[str]]=None, workflowSchemeIds: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk get workflow schemes

HTTP POST /rest/api/3/workflowscheme/read
Body (application/json) fields:
  - projectIds (list[str], optional)
  - workflowSchemeIds (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if projectIds is not None:
            _body['projectIds'] = projectIds
        if workflowSchemeIds is not None:
            _body['workflowSchemeIds'] = workflowSchemeIds
        rel_path = '/rest/api/3/workflowscheme/read'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_schemes(self, description: str, id: str, name: str, version: Dict[str, Any], defaultWorkflowId: Optional[str]=None, statusMappingsByIssueTypeOverride: Optional[list[Dict[str, Any]]]=None, statusMappingsByWorkflows: Optional[list[Dict[str, Any]]]=None, workflowsForIssueTypes: Optional[list[Dict[str, Any]]]=None, body_additional: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update workflow scheme

HTTP POST /rest/api/3/workflowscheme/update
Body (application/json) fields:
  - defaultWorkflowId (str, optional)
  - description (str, required)
  - id (str, required)
  - name (str, required)
  - statusMappingsByIssueTypeOverride (list[Dict[str, Any]], optional)
  - statusMappingsByWorkflows (list[Dict[str, Any]], optional)
  - version (Dict[str, Any], required)
  - workflowsForIssueTypes (list[Dict[str, Any]], optional)
  - additionalProperties allowed (pass via body_additional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultWorkflowId is not None:
            _body['defaultWorkflowId'] = defaultWorkflowId
        _body['description'] = description
        _body['id'] = id
        _body['name'] = name
        if statusMappingsByIssueTypeOverride is not None:
            _body['statusMappingsByIssueTypeOverride'] = statusMappingsByIssueTypeOverride
        if statusMappingsByWorkflows is not None:
            _body['statusMappingsByWorkflows'] = statusMappingsByWorkflows
        _body['version'] = version
        if workflowsForIssueTypes is not None:
            _body['workflowsForIssueTypes'] = workflowsForIssueTypes
        if 'body_additional' in locals() and body_additional:
            _body.update(body_additional)
        rel_path = '/rest/api/3/workflowscheme/update'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflow_scheme_mappings(self, id: str, workflowsForIssueTypes: list[Dict[str, Any]], defaultWorkflowId: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get required status mappings for workflow scheme update

HTTP POST /rest/api/3/workflowscheme/update/mappings
Body (application/json) fields:
  - defaultWorkflowId (str, optional)
  - id (str, required)
  - workflowsForIssueTypes (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultWorkflowId is not None:
            _body['defaultWorkflowId'] = defaultWorkflowId
        _body['id'] = id
        _body['workflowsForIssueTypes'] = workflowsForIssueTypes
        rel_path = '/rest/api/3/workflowscheme/update/mappings'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_scheme(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete workflow scheme

HTTP DELETE /rest/api/3/workflowscheme/{id}
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_scheme(self, id: int, returnDraftIfExists: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow scheme

HTTP GET /rest/api/3/workflowscheme/{id}
Path params:
  - id (int)
Query params:
  - returnDraftIfExists (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if returnDraftIfExists is not None:
            _query['returnDraftIfExists'] = returnDraftIfExists
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflow_scheme(self, id: int, defaultWorkflow: Optional[str]=None, description: Optional[str]=None, draft: Optional[bool]=None, id_body: Optional[int]=None, issueTypeMappings: Optional[Dict[str, Any]]=None, issueTypes: Optional[Dict[str, Any]]=None, lastModified: Optional[str]=None, lastModifiedUser: Optional[Dict[str, Any]]=None, name: Optional[str]=None, originalDefaultWorkflow: Optional[str]=None, originalIssueTypeMappings: Optional[Dict[str, Any]]=None, self_: Optional[str]=None, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Classic update workflow scheme

HTTP PUT /rest/api/3/workflowscheme/{id}
Path params:
  - id (int)
Body (application/json) fields:
  - defaultWorkflow (str, optional)
  - description (str, optional)
  - draft (bool, optional)
  - id (int, optional)
  - issueTypeMappings (Dict[str, Any], optional)
  - issueTypes (Dict[str, Any], optional)
  - lastModified (str, optional)
  - lastModifiedUser (Dict[str, Any], optional)
  - name (str, optional)
  - originalDefaultWorkflow (str, optional)
  - originalIssueTypeMappings (Dict[str, Any], optional)
  - self (str, optional)
  - updateDraftIfNeeded (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultWorkflow is not None:
            _body['defaultWorkflow'] = defaultWorkflow
        if description is not None:
            _body['description'] = description
        if draft is not None:
            _body['draft'] = draft
        if id_body is not None:
            _body['id'] = id_body
        if issueTypeMappings is not None:
            _body['issueTypeMappings'] = issueTypeMappings
        if issueTypes is not None:
            _body['issueTypes'] = issueTypes
        if lastModified is not None:
            _body['lastModified'] = lastModified
        if lastModifiedUser is not None:
            _body['lastModifiedUser'] = lastModifiedUser
        if name is not None:
            _body['name'] = name
        if originalDefaultWorkflow is not None:
            _body['originalDefaultWorkflow'] = originalDefaultWorkflow
        if originalIssueTypeMappings is not None:
            _body['originalIssueTypeMappings'] = originalIssueTypeMappings
        if self_ is not None:
            _body['self'] = self_
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        rel_path = '/rest/api/3/workflowscheme/{id}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def create_workflow_scheme_draft_from_parent(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Create draft workflow scheme

HTTP POST /rest/api/3/workflowscheme/{id}/createdraft
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/createdraft'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_default_workflow(self, id: int, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete default workflow

HTTP DELETE /rest/api/3/workflowscheme/{id}/default
Path params:
  - id (int)
Query params:
  - updateDraftIfNeeded (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if updateDraftIfNeeded is not None:
            _query['updateDraftIfNeeded'] = updateDraftIfNeeded
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_default_workflow(self, id: int, returnDraftIfExists: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get default workflow

HTTP GET /rest/api/3/workflowscheme/{id}/default
Path params:
  - id (int)
Query params:
  - returnDraftIfExists (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if returnDraftIfExists is not None:
            _query['returnDraftIfExists'] = returnDraftIfExists
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_default_workflow(self, id: int, workflow: str, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update default workflow

HTTP PUT /rest/api/3/workflowscheme/{id}/default
Path params:
  - id (int)
Body (application/json) fields:
  - updateDraftIfNeeded (bool, optional)
  - workflow (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        _body['workflow'] = workflow
        rel_path = '/rest/api/3/workflowscheme/{id}/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_scheme_draft(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete draft workflow scheme

HTTP DELETE /rest/api/3/workflowscheme/{id}/draft
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_scheme_draft(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get draft workflow scheme

HTTP GET /rest/api/3/workflowscheme/{id}/draft
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflow_scheme_draft(self, id: int, defaultWorkflow: Optional[str]=None, description: Optional[str]=None, draft: Optional[bool]=None, id_body: Optional[int]=None, issueTypeMappings: Optional[Dict[str, Any]]=None, issueTypes: Optional[Dict[str, Any]]=None, lastModified: Optional[str]=None, lastModifiedUser: Optional[Dict[str, Any]]=None, name: Optional[str]=None, originalDefaultWorkflow: Optional[str]=None, originalIssueTypeMappings: Optional[Dict[str, Any]]=None, self_: Optional[str]=None, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update draft workflow scheme

HTTP PUT /rest/api/3/workflowscheme/{id}/draft
Path params:
  - id (int)
Body (application/json) fields:
  - defaultWorkflow (str, optional)
  - description (str, optional)
  - draft (bool, optional)
  - id (int, optional)
  - issueTypeMappings (Dict[str, Any], optional)
  - issueTypes (Dict[str, Any], optional)
  - lastModified (str, optional)
  - lastModifiedUser (Dict[str, Any], optional)
  - name (str, optional)
  - originalDefaultWorkflow (str, optional)
  - originalIssueTypeMappings (Dict[str, Any], optional)
  - self (str, optional)
  - updateDraftIfNeeded (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if defaultWorkflow is not None:
            _body['defaultWorkflow'] = defaultWorkflow
        if description is not None:
            _body['description'] = description
        if draft is not None:
            _body['draft'] = draft
        if id_body is not None:
            _body['id'] = id_body
        if issueTypeMappings is not None:
            _body['issueTypeMappings'] = issueTypeMappings
        if issueTypes is not None:
            _body['issueTypes'] = issueTypes
        if lastModified is not None:
            _body['lastModified'] = lastModified
        if lastModifiedUser is not None:
            _body['lastModifiedUser'] = lastModifiedUser
        if name is not None:
            _body['name'] = name
        if originalDefaultWorkflow is not None:
            _body['originalDefaultWorkflow'] = originalDefaultWorkflow
        if originalIssueTypeMappings is not None:
            _body['originalIssueTypeMappings'] = originalIssueTypeMappings
        if self_ is not None:
            _body['self'] = self_
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        rel_path = '/rest/api/3/workflowscheme/{id}/draft'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_draft_default_workflow(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete draft default workflow

HTTP DELETE /rest/api/3/workflowscheme/{id}/draft/default
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_draft_default_workflow(self, id: int, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get draft default workflow

HTTP GET /rest/api/3/workflowscheme/{id}/draft/default
Path params:
  - id (int)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_draft_default_workflow(self, id: int, workflow: str, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Update draft default workflow

HTTP PUT /rest/api/3/workflowscheme/{id}/draft/default
Path params:
  - id (int)
Body (application/json) fields:
  - updateDraftIfNeeded (bool, optional)
  - workflow (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        _body['workflow'] = workflow
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/default'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_scheme_draft_issue_type(self, id: int, issueType: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete workflow for issue type in draft workflow scheme

HTTP DELETE /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}
Path params:
  - id (int)
  - issueType (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'issueType': issueType}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_scheme_draft_issue_type(self, id: int, issueType: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow for issue type in draft workflow scheme

HTTP GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}
Path params:
  - id (int)
  - issueType (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'issueType': issueType}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_workflow_scheme_draft_issue_type(self, id: int, issueType: str, issueType_body: Optional[str]=None, updateDraftIfNeeded: Optional[bool]=None, workflow: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set workflow for issue type in draft workflow scheme

HTTP PUT /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}
Path params:
  - id (int)
  - issueType (str)
Body (application/json) fields:
  - issueType (str, optional)
  - updateDraftIfNeeded (bool, optional)
  - workflow (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id, 'issueType': issueType}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issueType_body is not None:
            _body['issueType'] = issueType_body
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        if workflow is not None:
            _body['workflow'] = workflow
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def publish_draft_workflow_scheme(self, id: int, validateOnly: Optional[bool]=None, statusMappings: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Publish draft workflow scheme

HTTP POST /rest/api/3/workflowscheme/{id}/draft/publish
Path params:
  - id (int)
Query params:
  - validateOnly (bool, optional)
Body (application/json) fields:
  - statusMappings (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if validateOnly is not None:
            _query['validateOnly'] = validateOnly
        _body: Dict[str, Any] = {}
        if statusMappings is not None:
            _body['statusMappings'] = statusMappings
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/publish'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_draft_workflow_mapping(self, id: int, workflowName: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue types for workflow in draft workflow scheme

HTTP DELETE /rest/api/3/workflowscheme/{id}/draft/workflow
Path params:
  - id (int)
Query params:
  - workflowName (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _query['workflowName'] = workflowName
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_draft_workflow(self, id: int, workflowName: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue types for workflows in draft workflow scheme

HTTP GET /rest/api/3/workflowscheme/{id}/draft/workflow
Path params:
  - id (int)
Query params:
  - workflowName (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if workflowName is not None:
            _query['workflowName'] = workflowName
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_draft_workflow_mapping(self, id: int, workflowName: str, defaultMapping: Optional[bool]=None, issueTypes: Optional[list[str]]=None, updateDraftIfNeeded: Optional[bool]=None, workflow: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set issue types for workflow in workflow scheme

HTTP PUT /rest/api/3/workflowscheme/{id}/draft/workflow
Path params:
  - id (int)
Query params:
  - workflowName (str, required)
Body (application/json) fields:
  - defaultMapping (bool, optional)
  - issueTypes (list[str], optional)
  - updateDraftIfNeeded (bool, optional)
  - workflow (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _query['workflowName'] = workflowName
        _body: Dict[str, Any] = {}
        if defaultMapping is not None:
            _body['defaultMapping'] = defaultMapping
        if issueTypes is not None:
            _body['issueTypes'] = issueTypes
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        if workflow is not None:
            _body['workflow'] = workflow
        rel_path = '/rest/api/3/workflowscheme/{id}/draft/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_scheme_issue_type(self, id: int, issueType: str, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete workflow for issue type in workflow scheme

HTTP DELETE /rest/api/3/workflowscheme/{id}/issuetype/{issueType}
Path params:
  - id (int)
  - issueType (str)
Query params:
  - updateDraftIfNeeded (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'issueType': issueType}
        _query: Dict[str, Any] = {}
        if updateDraftIfNeeded is not None:
            _query['updateDraftIfNeeded'] = updateDraftIfNeeded
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow_scheme_issue_type(self, id: int, issueType: str, returnDraftIfExists: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow for issue type in workflow scheme

HTTP GET /rest/api/3/workflowscheme/{id}/issuetype/{issueType}
Path params:
  - id (int)
  - issueType (str)
Query params:
  - returnDraftIfExists (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id, 'issueType': issueType}
        _query: Dict[str, Any] = {}
        if returnDraftIfExists is not None:
            _query['returnDraftIfExists'] = returnDraftIfExists
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def set_workflow_scheme_issue_type(self, id: int, issueType: str, issueType_body: Optional[str]=None, updateDraftIfNeeded: Optional[bool]=None, workflow: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set workflow for issue type in workflow scheme

HTTP PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType}
Path params:
  - id (int)
  - issueType (str)
Body (application/json) fields:
  - issueType (str, optional)
  - updateDraftIfNeeded (bool, optional)
  - workflow (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id, 'issueType': issueType}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if issueType_body is not None:
            _body['issueType'] = issueType_body
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        if workflow is not None:
            _body['workflow'] = workflow
        rel_path = '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_workflow_mapping(self, id: int, workflowName: str, updateDraftIfNeeded: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete issue types for workflow in workflow scheme

HTTP DELETE /rest/api/3/workflowscheme/{id}/workflow
Path params:
  - id (int)
Query params:
  - workflowName (str, required)
  - updateDraftIfNeeded (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _query['workflowName'] = workflowName
        if updateDraftIfNeeded is not None:
            _query['updateDraftIfNeeded'] = updateDraftIfNeeded
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_workflow(self, id: int, workflowName: Optional[str]=None, returnDraftIfExists: Optional[bool]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get issue types for workflows in workflow scheme

HTTP GET /rest/api/3/workflowscheme/{id}/workflow
Path params:
  - id (int)
Query params:
  - workflowName (str, optional)
  - returnDraftIfExists (bool, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        if workflowName is not None:
            _query['workflowName'] = workflowName
        if returnDraftIfExists is not None:
            _query['returnDraftIfExists'] = returnDraftIfExists
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{id}/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def update_workflow_mapping(self, id: int, workflowName: str, defaultMapping: Optional[bool]=None, issueTypes: Optional[list[str]]=None, updateDraftIfNeeded: Optional[bool]=None, workflow: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set issue types for workflow in workflow scheme

HTTP PUT /rest/api/3/workflowscheme/{id}/workflow
Path params:
  - id (int)
Query params:
  - workflowName (str, required)
Body (application/json) fields:
  - defaultMapping (bool, optional)
  - issueTypes (list[str], optional)
  - updateDraftIfNeeded (bool, optional)
  - workflow (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'id': id}
        _query: Dict[str, Any] = {}
        _query['workflowName'] = workflowName
        _body: Dict[str, Any] = {}
        if defaultMapping is not None:
            _body['defaultMapping'] = defaultMapping
        if issueTypes is not None:
            _body['issueTypes'] = issueTypes
        if updateDraftIfNeeded is not None:
            _body['updateDraftIfNeeded'] = updateDraftIfNeeded
        if workflow is not None:
            _body['workflow'] = workflow
        rel_path = '/rest/api/3/workflowscheme/{id}/workflow'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_project_usages_for_workflow_scheme(self, workflowSchemeId: str, nextPageToken: Optional[str]=None, maxResults: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get projects which are using a given workflow scheme

HTTP GET /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages
Path params:
  - workflowSchemeId (str)
Query params:
  - nextPageToken (str, optional)
  - maxResults (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'workflowSchemeId': workflowSchemeId}
        _query: Dict[str, Any] = {}
        if nextPageToken is not None:
            _query['nextPageToken'] = nextPageToken
        if maxResults is not None:
            _query['maxResults'] = maxResults
        _body = None
        rel_path = '/rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_ids_of_worklogs_deleted_since(self, since: Optional[int]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get IDs of deleted worklogs

HTTP GET /rest/api/3/worklog/deleted
Query params:
  - since (int, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if since is not None:
            _query['since'] = since
        _body = None
        rel_path = '/rest/api/3/worklog/deleted'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_worklogs_for_ids(self, ids: list[int], expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get worklogs

HTTP POST /rest/api/3/worklog/list
Query params:
  - expand (str, optional)
Body (application/json) fields:
  - ids (list[int], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if expand is not None:
            _query['expand'] = expand
        _body: Dict[str, Any] = {}
        _body['ids'] = ids
        rel_path = '/rest/api/3/worklog/list'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def get_ids_of_worklogs_modified_since(self, since: Optional[int]=None, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get IDs of updated worklogs

HTTP GET /rest/api/3/worklog/updated
Query params:
  - since (int, optional)
  - expand (str, optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if since is not None:
            _query['since'] = since
        if expand is not None:
            _query['expand'] = expand
        _body = None
        rel_path = '/rest/api/3/worklog/updated'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def addon_properties_resource_get_addon_properties_get(self, addonKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get app properties

HTTP GET /rest/atlassian-connect/1/addons/{addonKey}/properties
Path params:
  - addonKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'addonKey': addonKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/atlassian-connect/1/addons/{addonKey}/properties'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def addon_properties_resource_delete_addon_property_delete(self, addonKey: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete app property

HTTP DELETE /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}
Path params:
  - addonKey (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'addonKey': addonKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def addon_properties_resource_get_addon_property_get(self, addonKey: str, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get app property

HTTP GET /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}
Path params:
  - addonKey (str)
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'addonKey': addonKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def addon_properties_resource_put_addon_property_put(self, addonKey: str, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set app property

HTTP PUT /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}
Path params:
  - addonKey (str)
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'addonKey': addonKey, 'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def dynamic_modules_resource_remove_modules_delete(self, moduleKey: Optional[list[str]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Remove modules

HTTP DELETE /rest/atlassian-connect/1/app/module/dynamic
Query params:
  - moduleKey (list[str], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        if moduleKey is not None:
            _query['moduleKey'] = moduleKey
        _body = None
        rel_path = '/rest/atlassian-connect/1/app/module/dynamic'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def dynamic_modules_resource_get_modules_get(self, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get modules

HTTP GET /rest/atlassian-connect/1/app/module/dynamic"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/atlassian-connect/1/app/module/dynamic'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def dynamic_modules_resource_register_modules_post(self, modules: list[Dict[str, Any]], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Register modules

HTTP POST /rest/atlassian-connect/1/app/module/dynamic
Body (application/json) fields:
  - modules (list[Dict[str, Any]], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        _body['modules'] = modules
        rel_path = '/rest/atlassian-connect/1/app/module/dynamic'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def app_issue_field_value_update_resource_update_issue_fields_put(self, Atlassian_Transfer_Id: str, updateValueList: Optional[list[Dict[str, Any]]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk update custom field value

HTTP PUT /rest/atlassian-connect/1/migration/field
Header params:
  - Atlassian-Transfer-Id (str, required)
Body (application/json) fields:
  - updateValueList (list[Dict[str, Any]], optional)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers['Atlassian-Transfer-Id'] = Atlassian_Transfer_Id
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if updateValueList is not None:
            _body['updateValueList'] = updateValueList
        rel_path = '/rest/atlassian-connect/1/migration/field'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def migration_resource_update_entity_properties_value_put(self, entityType: str, Atlassian_Transfer_Id: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Bulk update entity properties

HTTP PUT /rest/atlassian-connect/1/migration/properties/{entityType}
Path params:
  - entityType (str)
Header params:
  - Atlassian-Transfer-Id (str, required)
Body: application/json (list[Dict[str, Any]])"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers['Atlassian-Transfer-Id'] = Atlassian_Transfer_Id
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'entityType': entityType}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/atlassian-connect/1/migration/properties/{entityType}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def migration_resource_workflow_rule_search_post(self, Atlassian_Transfer_Id: str, ruleIds: list[str], workflowEntityId: str, expand: Optional[str]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Get workflow transition rule configurations

HTTP POST /rest/atlassian-connect/1/migration/workflow/rule/search
Header params:
  - Atlassian-Transfer-Id (str, required)
Body (application/json) fields:
  - expand (str, optional)
  - ruleIds (list[str], required)
  - workflowEntityId (str, required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers['Atlassian-Transfer-Id'] = Atlassian_Transfer_Id
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _body: Dict[str, Any] = {}
        if expand is not None:
            _body['expand'] = expand
        _body['ruleIds'] = ruleIds
        _body['workflowEntityId'] = workflowEntityId
        rel_path = '/rest/atlassian-connect/1/migration/workflow/rule/search'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='POST', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def service_registry_resource_services_get(self, serviceIds: list[str], headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Retrieve the attributes of service registries

HTTP GET /rest/atlassian-connect/1/service-registry
Query params:
  - serviceIds (list[str], required)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {}
        _query: Dict[str, Any] = {}
        _query['serviceIds'] = serviceIds
        _body = None
        rel_path = '/rest/atlassian-connect/1/service-registry'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='GET', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def delete_forge_app_property(self, propertyKey: str, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Delete app property (Forge)

HTTP DELETE /rest/forge/1/app/properties/{propertyKey}
Path params:
  - propertyKey (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = None
        rel_path = '/rest/forge/1/app/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='DELETE', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

    async def put_forge_app_property(self, propertyKey: str, body: Optional[Dict[str, Any]]=None, headers: Optional[Dict[str, Any]]=None) -> HTTPResponse:
        """Auto-generated from OpenAPI: Set app property (Forge)

HTTP PUT /rest/forge/1/app/properties/{propertyKey}
Path params:
  - propertyKey (str)
Body: application/json (str)"""
        if self._client is None:
            raise ValueError('HTTP client is not initialized')
        _headers: Dict[str, Any] = dict(headers or {})
        _headers.setdefault('Content-Type', 'application/json')
        _path: Dict[str, Any] = {'propertyKey': propertyKey}
        _query: Dict[str, Any] = {}
        _body = body
        rel_path = '/rest/forge/1/app/properties/{propertyKey}'
        url = self.base_url + _safe_format_url(rel_path, _path)
        req = HTTPRequest(method='PUT', url=url, headers=_as_str_dict(_headers), path_params=_as_str_dict(_path), query_params=_as_str_dict(_query), body=_body)
        resp = await self._client.execute(req)
        return resp

def _safe_format_url(template: str, params: Dict[str, object]) -> str:
    try:
        return template.format_map(_SafeDict(params))
    except Exception:
        return template

def _to_bool_str(v: Union[bool, str, int, float]) -> str:
    if isinstance(v, bool):
        return 'true' if v else 'false'
    return str(v)

def _serialize_value(v: Union[bool, str, int, float, list, tuple, set, None]) -> str:
    if v is None:
        return ''
    if isinstance(v, (list, tuple, set)):
        return ','.join((_to_bool_str(x) for x in v))
    return _to_bool_str(v)

def _as_str_dict(d: Dict[str, Any]) -> Dict[str, str]:
    return {str(k): _serialize_value(v) for (k, v) in d.items()}

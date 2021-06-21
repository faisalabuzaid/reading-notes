# Permissions & Postgresql 

## Permissions

  - Authentication or identification by itself is not usually sufficient to gain access to information or code.
  - For that, the entity requesting access must have authorization.
  - Together with authentication and throttling, permissions determine whether a request should be granted or denied access.
  - The simplest style of permission would be to allow access to any authenticated user, and deny access to any unauthenticated user.
  - This corresponds to the IsAuthenticated class in REST framework.
  - A slightly less strict style of permission would be to allow full access to authenticated users, but allow read-only access to unauthenticated users. 
  - This corresponds to the IsAuthenticatedOrReadOnly class in REST framework.
  
  - **How permissions are determined**:
    - Permissions in REST framework are always defined as a list of permission classes.
    - Before running the main body of the view each permission in the list is checked.
    - If any permission check fails an exceptions.PermissionDenied or exceptions.NotAuthenticated exception will be raised, and the main body of the view will not run.
    - When the permissions checks fail either a "403 Forbidden" or a "401 Unauthorized" response will be returned, according to the following rules:

       - The request was successfully authenticated, but permission was denied. — An HTTP 403 Forbidden response will be returned.
       - The request was not successfully authenticated, and the highest priority authentication class does not use WWW-Authenticate headers. — An HTTP 403 Forbidden response will be returned.
       - The request was not successfully authenticated, and the highest priority authentication class does use WWW-Authenticate headers. — An HTTP 401 Unauthorized response, with an appropriate WWW-Authenticate header will be returned.
    
    - **Object level permissions**:
        - REST framework permissions also support object-level permissioning. 
        - Object level permissions are used to determine if a user should be allowed to act on a particular object, which will typically be a model instance.
        - Object level permissions are run by REST framework's generic views when .get_object() is called.
        - As with view level permissions, an exceptions.PermissionDenied exception will be raised if the user is not allowed to act on the given object.
        - This will either raise a PermissionDenied or NotAuthenticated exception, or simply return if the view has the appropriate permissions.
        


-   ## API Reference:
    - **AllowAny**: permission class will allow unrestricted access, regardless of if the request was authenticated or unauthenticated.
    - **IsAuthenticated**: permission class will deny permission to any unauthenticated user, and allow permission otherwise.This permission is suitable if you want your API to only be accessible to registered users.
    - **IsAdminUser**:  permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.
    - **IsAuthenticatedOrReadOnly**: will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write permissions to authenticated users.
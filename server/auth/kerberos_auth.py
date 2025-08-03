from fastapi import Depends, HTTPException, status, Request

class KerberosAuth:
    async def __call__(self, request: Request) -> bool:
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Negotiate "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required",
                headers={"WWW-Authenticate": "Negotiate"},
            )
        
        return True
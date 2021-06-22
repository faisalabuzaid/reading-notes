# Authentication & Production Server 

##  Introduction to JSON Web Tokens

  - **What is JSON Web Token?**
    - JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
    - This information can be verified and trusted because it is digitally signed.
    - JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA. 
  
  - **When should you use JSON Web Tokens?**
  
    - **Authorization:** This is the most common scenario for using JWT. Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token
    - **Information Exchange:** JSON Web Tokens are a good way of securely transmitting information between parties. Because JWTs can be signed—for example, using public/private key pairs—you can be sure the senders are who they say they are. 
  
  - **What is the JSON Web Token structure?**
    - SON Web Tokens consist of three parts separated by dots (.), which are:
        - **Header**: consists of two parts: the type of the token, which is JWT, and the signing algorithm being used, such as HMAC SHA256 or RSA.
        - **Payload**: contains the claims. Claims are statements about an entity (typically, the user) and additional data. three types of claims: registered, public, and private claims.
        - **Signature**: To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.
    -  a JWT typically looks like: xxxxx.yyyyy.zzzzz
    
  - **Why should we use JSON Web Tokens?**
    - As JSON is less verbose than XML, when it is encoded its size is also smaller, making JWT more compact than SAML. This makes JWT a good choice to be passed in HTML and HTTP environments.
    - JSON parsers are common in most programming languages because they map directly to objects. Conversely, XML doesn't have a natural document-to-object mapping. This makes it easier to work with JWT than SAML assertions.

---

## How to Use JWT Authentication with Django REST Framework
  - JWT stand for JSON Web Token and it is an authentication strategy used by client/server applications where the client is a Web application using JavaScript and some frontend framework like Angular, React or VueJS.
  - **How JWT Works?**
    - `curl http://127.0.0.1:8000/hello/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY'`
    - The JWT is acquired by exchanging an username + password for an access token and an refresh token.
    - The access token is usually short-lived (expires in 5 min or so, can be customized though).
    - The refresh token lives a little bit longer (expires in 24 hours, also customizable). 
    - It is comparable to an authentication session. After it expires, you need a full login with username + password again.
    
    - ```
    
        header = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
        payload = eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9
        signature = Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY
        
      ```
    - header

                {
                  "typ": "JWT",
                  "alg": "HS256"
                }
                
    - payload

              {
                "token_type": "access",
                "exp": 1543828431,
                "jti": "7f5997b7150d46579dc2b49167097e7b",
                "user_id": 1
              }
              
     - signature: 
        - The signature is issued by the JWT backend, using the header base64 + payload base64 + SECRET_KEY.
        - Upon each request this signature is verified.
        - If any information in the header or in the payload was changed by the client it will invalidate the signature.
        - The only way of checking and validating the signature is by using your application’s SECRET_KEY.
        - Among other things, that’s why you should always keep your SECRET_KEY secret!
        

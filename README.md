

### Run Server
uvicorn main:app --reload



### AWS Setup
- name bucket
- enabled ACLs
- set object writer
- disable block public access
- enable transfer acceleration


#### AWS Permissions

Bucket Policy
```
{"Version": "2012-10-17",
"Statement": [
    {
        "Sid": "myPolicy",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "*",
        "Resource": [
            "arn:aws:s3:::YOUR_BUCKET_NAME/*",
            "arn:aws:s3:::YOUR_BUCKET_NAME"
        ]
    }
]}

```


CORS Settings
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "ETag"
        ],
        "MaxAgeSeconds": 3000
    }
]
```
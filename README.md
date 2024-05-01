# Multipart File Uploading with Python & JavaScript


### Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### ENV Vars
- create a .env file in your root directory
```
AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME
AWS_DEFAULT_REGION=YOUR_REGION_NAME
AWS_ACCESS_KEY_ID=_YOUR_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET
```

### Run Server
uvicorn main:app --reload


### AWS Setup
- name bucket
- enabled ACLs
- set object writer
- disable block public access
- enable transfer acceleration (optional and not used in example)


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
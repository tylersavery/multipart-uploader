# Multipart File Uploading with Python & JavaScript

This repository is a resource for my video tutorial "Beyond 5GB: How to Tackle Large File Uploads with AWS S3." The tutorial can be found [here](https://www.youtube.com/watch?v=HkF3_GLVKEg).

Welcome to this comprehensive tutorial where we delve into the world of large file uploads using AWS S3! If you're interested in the challenge of handling files large file uploads, this video is tailor-made for you.

In this guide, we explore the multipart upload feature of AWS S3, which not only boosts the upload efficiency but also enhances the reliability of your file transfers. Learn how to implement multipart uploads directly from your browser, with Python acting as a powerful intermediary to coordinate with AWS. Save on server processing time and bandwidth by having your users upload directly to S3.

What You Will Learn:

- Overview: Setting the stage to the options available to you for file uploads, and the upsides of multipart
- Basics of Multipart Uploads: Understand the fundamentals and advantages of using multipart uploads for large files.
- Setting Up Your Environment: Step-by-step guidance on configuring your Python environment (with fastapi!) to interact with AWS S3.
- Hands-On Coding: Watch and code along as we demonstrate the complete process to initiate, manage, and complete multipart uploads.

Whether you are a developer, a data scientist, or just a tech enthusiast, this tutorial will equip you with the skills to efficiently manage large file uploads to AWS S3. Perfect your uploads and ensure your large data files are handled with precision and ease.

### Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


### ENV Vars
Create a .env file in your root directory with the following contents. Update the values to match your config.

```
AWS_STORAGE_BUCKET_NAME=YOUR_BUCKET_NAME
AWS_DEFAULT_REGION=YOUR_REGION_NAME
AWS_ACCESS_KEY_ID=YOUR_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET
```

### Run Server
```
uvicorn main:app --reload
```


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
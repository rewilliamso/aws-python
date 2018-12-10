#!/usr/bin/python
# -*_ coding: utf-8 -*-

"""Webotron: Deploy websites with AWS.

Webotron automate process of deploying sites to aws.
- Configure AWS S3 buckets
    - Create them
    - Set them up for static web hosting
    - Deploy local files to them
- Configure DNS with AWS route53
- Configure a content delivery network and SSL with aws
"""
import boto3
import click

from bucket import BucketManager

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
#s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploy websites to AWS."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-buckets-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List files in s3 buckets."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    bucket_manager.sync_bucket(pathname, bucket)


if __name__ == '__main__':
    cli()

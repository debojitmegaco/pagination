import boto3
client = boto3.client("resourcegroupstaggingapi")
token = None
while True:
  response = client.get_resources(
      PaginationToken=token,
      TagFilters=[
          {
              'Key': 'string',
              'Values': [
                  'string',
              ]
          },
      ],
      ResourcesPerPage=123,
      TagsPerPage=123,
      ResourceTypeFilters=[
          'string',
      ],
      IncludeComplianceDetails=True|False,
      ExcludeCompliantResources=True|False,
      ResourceARNList=[
          'string',
      ]
  )
  for ResourceTagMappingList in page.get("ResourceTagMappingList"):
    print(ResourceTagMappingList)
  try:
      token = response['PaginationToken']
  except KeyError:
      break

aws s3 ls >> bucketlist.txt 

#create a txt file named bucketlist and write the list of s3 buckets into it
aws s3api create-bucket --bucket cloudreality --region us-east-1  

#create an s3 bucket in us-east-1 named cloudreality
aws s3 cp bucketlist.txt s3://cloudreality/  

#copy the dump text file and paste it into the cloudreality s3 bucket

echo "(It was a success yaaaaay!)"


aws cloudformation create-stack --stack-name myteststack --template-body file://templates/s3.yaml

aws cloudformation create-stack --stack-name myteststack --template-body file://templates/s3.yaml
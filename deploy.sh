ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP "docker login -u gitlab-ci-token -p $CI_BUILD_TOKEN $CI_REGISTRY"
ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP "docker pull $TAG_COMMIT"
ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP "docker container rm -f backend || true"
ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP "docker run --net elastic -d -p 8000:8000 --name backend $TAG_COMMIT"

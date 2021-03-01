helm package temporal-matching/deps/temporal-matching-frontend/
helm package temporal-matching/deps/temporal-matching-server/
helm package temporal-matching/
# Push the helm package to local repo, but can be anywhere
curl --data-binary "@temporal-matching-server-$1.tgz" http://localhost:8080/api/charts?force
curl --data-binary "@temporal-matching-frontend-$1.tgz" http://localhost:8080/api/charts?force
curl --data-binary "@temporal-matching-$1.tgz" http://localhost:8080/api/charts?force
helm repo update
helm install chartmuseum/temporal-matching-server
helm install chartmuseum/temporal-matching-frontend

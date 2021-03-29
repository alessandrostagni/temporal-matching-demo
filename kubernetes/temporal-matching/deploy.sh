helm package charts/temporal-matching-frontend/
helm package charts/temporal-matching-server/
# Push the helm package to local repo, but can be anywhere
curl --data-binary "@temporal-matching-server-$1.tgz" http://localhost:8080/api/charts?force
curl --data-binary "@temporal-matching-frontend-$1.tgz" http://localhost:8080/api/charts?force
helm repo update
helm install temporal-matching-server-$1 chartmuseum/temporal-matching-server 
helm install temporal-matching-frontend-$1 chartmuseum/temporal-matching-frontend

stuff here is to replicate issue i submitted here:
https://github.com/SergeyPirogov/webdriver_manager/issues/266

-mrkprdo

Instructions:
- Run docker build command below:
- The container will mount results folder and save output to `test_results.txt` file.
-

Docker Build:
```
docker-compose up --build --force-recreate --no-deps --detach
```

If there is no result saved, maybe the mounted volume need permission update
```
chmod a+rwx results
```
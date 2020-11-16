# Static Files

In order to provide static files like javascript, images, css, etc, you put the corresponding file/directory in the *http/* and edit/create the file *http/.static* with a line for each resource to be server as static.

```
robots.txt
img/
cs/
js/
```

A second wourld can be provided to serve the content at a specific location, in the next example the content of *my_images/* will be available from the URL */site_images/*
```
my_images/ /site_images/
```


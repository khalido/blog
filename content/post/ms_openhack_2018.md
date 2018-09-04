---
title: "Microsoft OpenHack 2018 Sydney"
date: 2018-09-04
draft: true
tags:
- meetup
---

My first ever hackathon! Or so it was called. Notes:

## Day One: Azure basics

First up, we learned about and how to use Microsoft Azure. I hadn't used it and it seems to have rebuilt AWS but with a nicer interface. These massive clouds are all so wide and deep that just clicking around in the interface can take days since things keep coming up.

Our team spun up a Ubuntu Data Science Virtual Machine (DSVM) on Azure, which comes with JupyterHub ready to run out. It was suprinsingly easy. Still, JupyterHub needs to work on a multiuser interface, if not a full GoogleDocs thingamajig, at least one where other users can hop onto your notebook as you drive it.

The hackathon was suprisingly straightforward - learned various bits and bobs, one main one being the [Microsoft Custom Vision Service](https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/) which looks somewhat similar [Amazon Rekognition](https://aws.amazon.com/rekognition/) or [Google Cloud Vision](https://cloud.google.com/vision/).

The python api is a little bit tricky since every cloud provider has their own vision of how their api's should function, so it takes getting used to a bit, but once thats done its suprisingly easy to upload training images to custom vision, train the model (it automagics whatever its transfer learning from) and then send it images to predict on. Presto, barely a page of code and what used to be rocket science is now being rolled out all the world.

Also covered preprocessing images using the [Pillow image libary](https://pillow.readthedocs.io/en/5.2.x/). Its slower then opencv and others, but its so much nicer to write.

Anyways, with all this fancy deep learning in the clouds and using apis and what not, I liked this bit of code which preprocessed all the training images:

```python
def preprocess_all_images_in_dir(img_dir="gear_images/", 
                              processed_dir="gear_images_processed/", 
                              show_images=False):
    """processes all the images in the subdirectories of the passed in img_dir
       and saves them in subdirectories of the same name in the processed_dir"""

    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    for d in os.listdir(img_dir):
        cur_dir = img_dir + d
        new_dir = processed_dir + d

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        for img in os.listdir(cur_dir):
            im = pre_process_image(cur_dir +"/"+ img)
            if show_images:
                clear_output(wait=True)
                display(im)
            im.save(new_dir + "/" + img)

preprocess_all_images_in_dir()
```

The hard parts are being all out sourced, like deep learning, so it makes sense that the simple plumbing work is what many coders end up coding. It's amazing how quickly now you can get things done by plumbing bits together. And Ideally, services is where its all at now.
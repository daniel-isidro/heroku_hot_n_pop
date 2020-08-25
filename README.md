![logo](https://github.com/daniel-isidro/heroku_hot_n_pop/blob/master/hnp_logo.jpeg)

Repository for the front end web app of the **Hot'n'Pop Song Machine** project, a Machine Learning song popularity predictor, that uses the Streamlit app framework and web hosting on Heroku.

The Github repository of the Hot'n'Pop Song Machine project can be found at https://github.com/daniel-isidro/hot_n_pop_song_machine.

You can have a live demo of the web app [here](https://hot-n-pop-song-machine.herokuapp.com).

# Installation

### Streamlit

Streamlit’s open-source app framework is an easy way to create web apps, all in Python, for free. You can find more info at https://www.streamlit.io

For installing Streamlit, according to the source documentation:

1. Make sure that you have Python 3.6 or greater installed.

2. Install Streamlit using PIP:
```
$ pip install streamlit
```

3. Run the hello world app:
```
$ streamlit hello
```

4. That’s it! In the next few seconds the sample app will open in a new tab in your default browser.

### Heroku deployment

Heroku is a platform as a service (PaaS) which can be used to run applications fully in the cloud. To deploy the app you will first need to create a free account on [Heroku](https://signup.heroku.com/dc). You can use a Github repository as a file source on Heroku. That way every time a file is updated on the Github repository, a redeployment to Heroku with those changes is automagically triggered. We need to have these files in that Github repository:

1. **hotnpop.py**

  Python code of the web app.

2. **requirements.txt**

  The requirements.txt file lists the app dependencies together. When an app is deployed, Heroku reads this file and installs the appropriate Python dependencies using the pip install -r command. To do this locally, you can run the following command:
  ```
  pip install -r requirements.txt
  ```
  Note: Postgres must be properly installed in order for this step to work properly.

3. **setup.sh**

  With this file a streamlit folder with a config.toml file is created.

4. **Procfile**

  A text file in the root directory of your application, to explicitly declare what command should be executed to start the app.

5. **model.pkl**

  The pickled ML model.

6. **settings.env**

  Text file containing user tokens for the Spotify Web API.

7. **hnp_logo.jpg**

  Top image in the web page.

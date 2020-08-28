![logo](https://github.com/daniel-isidro/heroku_hot_n_pop/blob/master/hnp_logo.jpeg)

Repository for the front end web app of the **Hot'n'Pop Song Machine** project, a Machine Learning song popularity predictor, that uses the Streamlit app framework and web hosting on Heroku.

The Github repository of the full **Hot'n'Pop Song Machine** project can be found **[here](https://github.com/daniel-isidro/hot_n_pop_song_machine)**.

You can play with a live demo of the web app **[here](https://hot-n-pop-song-machine.herokuapp.com)**.

# Installation

### Streamlit

Streamlit’s open-source app framework is an easy way to create web apps, all in Python, for free. You can find more info at https://www.streamlit.io.

For **installing Streamlit**, according to the source documentation:

1. Make sure that you have Python 3.6 or greater installed.

2. Install Streamlit using PIP:
```
$ pip install -q streamlit==0.65.2
```

3. Run the hello world app:
```
$ streamlit hello
```

4. Done. In the next few seconds the sample app will open in a new tab in your default browser.

### Heroku deployment

Heroku is a platform as a service (PaaS) which can be used to run applications fully in the cloud. To deploy your app you will first need to create a **free account** on [Heroku](https://signup.heroku.com/dc).

After signing up, in the **Heroku Dashboard**, you can use a Github repository as a **deployment method** on Heroku. You have to connect your Heroku app to the Github repository of your choice, and then turn on **'Automatic deploys'**. That way every time a file is updated on the Github repository, a redeployment to Heroku with those changes is automagically triggered.

You will need to have these files in the Github repository:

1. **hotnpop.py**

Python code of the web app.

2. **requirements.txt**

The requirements.txt file lists the app dependencies together. When an app is deployed, Heroku reads this file and installs the appropriate Python dependencies using the pip install -r command. To do this locally, you can run the following command:
```
pip install -r requirements.txt
```
Note: Postgres must be properly installed in order for this step to work properly.

3. **setup.sh**

With this file a Streamlit folder with a config.toml file is created.

4. **Procfile**

A text file in the root directory of your application, to explicitly declare what command should be executed to start the app.

5. **model.pkl**

The pickled ML model.

6. **hnp_logo.jpg**

Top image on the web page.

**Config Vars**

In order to use your secret Spotify web API credentials in the web app, you will have to set up two config vars, **SPOTIPY_CLIENT_ID** and **SPOTIPY_CLIENT_SECRET**, in the Settings area of the Heroku Dashboard.

![Config Vars](https://github.com/daniel-isidro/heroku_hot_n_pop/blob/master/config_vars.png)

They will act as Python environment vars. Please enter keys and values without quotes.

**URL**

Heroku will create a free subdomain for your web app, like http://webapp.herokuapp.com, but you can also specify a custom domain in the Heroku Dashboard.

That's it! Remember you can play with a live demo of the **Hot'n'Pop Song Machine** web app **[here](https://hot-n-pop-song-machine.herokuapp.com)**.

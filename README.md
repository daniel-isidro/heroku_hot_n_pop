Repository for the web app of the Hot'n'Pop project that uses the Streamlit app framework and hosting on Heroku.

The repository of the Hot'n'Pop project can be found at https://github.com/daniel-isidro/hot_n_pop_song_machine.

You can have a live demo at https://hot-n-pop-song-machine.herokuapp.com

# Installation

## Streamlit

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

## Heroku deployment

Heroku is a platform as a service (PaaS) which can be used to run applications fully in the cloud. To deploy the app you will first need to create a free account on Heroku at https://signup.heroku.com/dc. You can use a Github repository as a file source on Heroku. In our case, for the web app to be deployed automagically, we need to have these files in that repository:

* hotnpop.py
* requirements.txt
* setup.sh
* Procfile
* model.pkl
* settings.env
* hnp_logo.jpg

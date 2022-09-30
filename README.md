<h1 align="center">
  <a href="fetch_rewards_coding_exercise.git">
    <!-- Please provide path to your logo here -->
    <div style="font-family: 'Shadows Into Light', cursive; font-size: x-large; color: Black">Fetch Rewards Coding Exercise - Backend Software Engineering</div>
  </a>
</h1>

<div align="center">
<br />

[![code with love by asya_code](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-asya_code-ff1414.svg?style=flat-square)](https://github.com/asya-code)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Launch your server](#launch-your-server)

</details>

---

## About
<p>
<a href=https://fetch-hiring.s3.us-east-1.amazonaws.com/points.pdf>
<div style="font-family: 'Shadows Into Light', cursive; color: Black">Exercise requirements</div>
</a>
</p>

<br>


<img src="static/images/NAME.png" title="Title" width="100%"> 
<br>


### Built With

Backend is powered by Python with Flask web framework and SQLAlchemy as its ORM, PostgreSQL for database.
<br>


## Features
<p>
<ul>
    <li> Add transactions for a specific payer and date. </li>
    <li> Spend points using and return a list of payer : points pairs for each call. </li>
    <li> Return all payer point balances. </li>
</ul>
<p>
<img src="static/images/NAME.png" title="NAME" width="100%"> 


## Getting Started

### Installation

Retrieve an entire repository from a hosted location via URL
<br>
<p> &nbsp <b> git clone https://github.com/asya-code/fetch_rewards_coding_exercise.git </b> </p>

You’d then create a virtual environment:

<p> &nbsp <b> virtualenv env </b> </p>

Next, you’d activate that environment:
<br>

<p> &nbsp <b> source env/bin/activate </b> </p>

Finally, you’d use pip3 to install all of the requirements:
<br>

<p> &nbsp <b> (env) $ pip3 install -r requirements.txt </b> </p>
The -r option lets you supply a text file in the format pip3 freeze produces. This command should install all of the listed libraries.

To confirm that the correct packages are installed, you’d just run:
<br>

<p> &nbsp <b> pip3 freeze </b> </p>

### Launch your server

Once you’ve set up your virtual environment, activated it, and installed Flask, you should just be able to type:
<br>
<p> &nbsp <b> python3 server.py </b> </p>


# pymoji

[![Build Status](https://secure.travis-ci.org/michaeljoseph/pymoji.png)](http://travis-ci.org/michaeljoseph/pymoji)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/pymoji.png?label=ready)](https://waffle.io/michaeljoseph/pymoji) [![pypi version](https://badge.fury.io/py/pymoji.png)](http://badge.fury.io/py/pymoji)
[![# of downloads](https://pypip.in/d/pymoji/badge.png)](https://crate.io/packages/pymoji?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/pymoji/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/pymoji?branch=master)

## Overview

Emits HTML from Emoji.

## Usage

Install `pymoji`:

    pip install pymoji

Run it:

	$ pymoji :heart:
	<img class="emoji" title="heart" alt="heart" height="20" width="20" src="http://a248.e.akamai.net/assets.github.com/images/icons/emoji/heart.png" align="top">

With or without the `:`:

	$ pymoji heart_eyes
	<img class="emoji" title="heart_eyes" alt="heart_eyes" height="20" width="20" src="http://a248.e.akamai.net/assets.github.com/images/icons/emoji/heart_eyes.png" align="top">

Or a phrase:

    $ pymoji "this is :+1:"
    this is <img class="emoji" title="+1" alt="+1" height="20" width="20" src="http://a248.e.akamai.net/assets.github.com/images/icons/emoji/+1.png" align="top">

## Documentation

[API Documentation](http://pymoji.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 pymoji tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir

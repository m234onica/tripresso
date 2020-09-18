from flask import Blueprint, render_template, jsonify, request, g, redirect, flash, url_for

site = Blueprint('site', __name__)

@site.route()
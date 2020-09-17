from flask import Blueprint, render_template, jsonify, request, g, redirect, flash, url_for

cms = Blueprint('cms', __name__)


from flask import Flask, render_template, session, request, redirect
from __main__ import app
import os
from postgres import getSpots, inputOccupancy, deleteOccupancy
from middleware import formatSpotData, externalOccupancy

@app.route('/losangeles')
def losAngeles():
    deleteOccupancy.deleteOccupancy("LA")
    inputOccupancy.inputOccupancyLosAngeles(externalOccupancy.getOccupancy("LA"))
    data = getSpots.get_spots("LA")
    formattedData = formatSpotData.formatLosAngeles(data)
    
    return render_template(
        'losangeles.html', 
        data=formattedData
    )


@app.route('/sanfrancisco')
def sanFrancisco():
    #deleteOccupancy.deleteOccupancy("SF")
    #inputOccupancy.inputOccupancySanFrancisco(externalOccupancy.getOccupancy("SF"))
    #formattedData = formatSpotData.formatSanFrancisco(data)
    #formattedData = formatSpotData.formatSanFrancisco(externalOccupancy.getOccupancy("SF"))
    return render_template(
        'sanfrancisco.html'
    )
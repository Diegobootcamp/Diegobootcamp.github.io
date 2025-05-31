# Importing required functions 
import os
import pandas as pd
import matplotlib
import seaborn as sns
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from flask import Flask, render_template , request
import csv


# Flask constructor 
app = Flask(__name__) 

# Generate a scatter plot and returns the figure 
def get_plot():
	df = pd.read_csv('train.csv')
	sns.countplot(x="survived", hue="sex", data=df)
	plt.title("Gráfico de Supervivencia por Género")
	plt.xlabel("Sobrevivió (0 = No, 1 = Sí)")
	plt.ylabel("Cantidad")
	return plt 

# Root URL 
@app.get('/') 
def single_converter(): 
	# Get the matplotlib plot 
	plot = get_plot() 

	# Save the figure in the static directory 
	plot.savefig(os.path.join('static', 'images', 'plot.png')) 

	return render_template('index.html') 

# Main Driver Function 
if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run(debug=True)
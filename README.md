                                Solar EV Calculator

A simple Flask web app that estimates how much solar energy you can use to charge an electric vehicle.
You choose your state, solar system size, EV model, and daily miles, and the app calculates:

Daily solar energy (kWh)

Estimated miles you can drive from that energy

Battery size of the selected EV

How many sunny days it would take to fully charge the battery

                                          Features

All 50 U.S. states with average sun‑hours

Large list of EV models (past + present)

Clean, simple interface

Built with Flask + HTML

Easy to run locally or deploy online

                                        How to Run

pip install -r requirements.txt
python main.py
then open http://127.0.0.1:5000

                                        Files
main.py — Flask app

index.html — main page

help.html — help page

requirements.txt — dependencies

render.yaml — deployment config

h

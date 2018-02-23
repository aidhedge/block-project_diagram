# block-montecarlo_simulation
FROM python:3
EXPOSE 7008
ENV FLASK_DEBUG=1
ENV PORT=7008
RUN pip install flask
RUN pip install cerberus
RUN pip install requests
RUN pip install networkx

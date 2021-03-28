# temporal_matching_demo

This project refers to the [Temporal Matching paper](https://arxiv.org/abs/1812.08615).

Specifically, this project has as main focus **Theorem 1**, in which a reduction of the Temporal Matching problem to 3-SAT is shown.
The web application allows the user to input a formula and an assignment for its symbols, together with the value of γ.

An example of input is the following:

- Formula: `(w or x or y) and (w or x or z)`

- Assignment: 

```
{
    "w": "true",
    "x": "true",
    "y": "false",
    "z": "true"
}
```

- Gamma: 3

After the Compute button is pressed, the corresponding Link Stream and Matching will be built according to the paper.

This project has the only didactic purpose of giving a visualisation on how the Link Stream and Matching construction works from a 3-sat formula.

## Technology stack

The web server that takes care of the Link Stream and Matching computation is implemented in Python and contained in the `app` folder.
I have implemented the Link Stream as a list of [NetworkX](https://networkx.org/) graphs. The code for the link stream implementation is contained in the `app/LinkStream` package.

The frontend has been implemented in React. The code can be found in the `frontend` folder.

The application has been deployed in Kubernetes through [Helm](https://helm.sh/) charts.
The charts can be found inside the `Kubernetes` folder.
The charts are not currently installed online as I do not hold an Helm repo.
So far I have been using [Charmuseum](https://chartmuseum.com/#Instructions) locally.

Given a chart repository and a kubernetes config, the `kubernetes/deploy.sh` script takes care of deploying the whole stack to a target cluster.
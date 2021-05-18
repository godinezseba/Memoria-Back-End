# Prototype Climate Impact Rating Server & API

This code provides a starter kit that will allow you to standup a prototype Climate Impact Rating (CIR) server, with a consumer API and a backend CouchDB database instance in IBM Cloudant.

Refer to the [tutorial](https://developer.ibm.com/tutorials/provision-a-couchdb-instance-using-cloudant-cfc-starter-kit-2/) for installation and usage instructions.

This solution starter was initially created at the United Nations Human Rights Office in Geneva, Switzerland on February 27-28, 2020, and built out over following 4 weeks. It features contributions by technologists from JPMorgan Chase, Persistent Systems, IBM, and Red Hat.

## Authors

- Vincent Batts - Red Hat
- Binu Midhun - IBM
- Mark Meiklejohn - JPMorgan Chase
- Roberto Mosqueda - Persistent Systems
- Henry Nash - IBM

## License

This solution starter is made available under the [Apache 2 License](LICENSE).

## Ejecución

`sudo docker build . -t cir-api-server`

`sudo docker run -p 8080:8080 cir-api-server`

# Climate Impact Rating (CIR) Server

This is a PoC of an API server to manage Climate Impact data for products, for the 2020
[Call-For-Code](https://callforcode.org/), from the [Energy Sustainability
team](https://github.com/Call-for-Code/solution-starter-kit-energy-2020).

This is intended as an example to enable experimentation, as described in the main [README](../README.md).

## Next goals of this code repo

- more complete API support
- include geo-summary data
- implement example climate rating algorithms, that summarize the impact of a product

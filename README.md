#  FastAPI Calculator App

A simple microservice built with **FastAPI** that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

This project follows the [12-Factor App](https://12factor.net/) methodology with clean structure, Docker support, environment-based configuration, pre-commit hooks, testing, and CI/CD pipeline via GitHub Actions.

---

##  Features

- Simple `/calculate` POST endpoint
- Supports `+`, `-`, `*`, `/` operations
- Built with FastAPI and Pydantic
- Dockerized for easy deployment
- Swagger & ReDoc documentation
- Unit tested with pytest
- GitHub Actions workflow for CI
- Environment-based config using `.env`

---

##  How to Run

### ▶ Locally (with Python)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-calculator.git
   cd fastapi-calculator

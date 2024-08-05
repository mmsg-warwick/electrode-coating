import pybamm


class Newtonian(pybamm.BaseModel):
    def __init__(self, name="Newtonian model"):
        super().__init__(name=name)  # This initiates the parent class

        ##################
        # Define parameter
        ##################
        # for velocity_profile and thickness_convergence
        P = pybamm.Parameter("Pressure [Pa]")
        U = pybamm.Parameter("Coating speed [m.s-1]")

        # for viscosity_profile
        mu = pybamm.Parameter("Newtonian viscosity [Pa]")
        gamma = pybamm.Parameter("Shear strain [s-1]")
        # m = pybamm.Parameter("Exponent parameter [t]")

        # for analytical coating thickness
        A_1 = pybamm.Parameter("Integration constant 1")
        A_2 = pybamm.Parameter("Integration constant 2")
        H_g = pybamm.Parameter("Coating gap [m]")
        n = pybamm.Parameter("Power-law index")

        #################
        # Define variables
        #################
        # for velocity_profile and thickness_convergence
        u = pybamm.Variable("Velocity [m.s-1]", domain="coating")
        y = pybamm.SpatialVariable("y [m]", domain="coating", coord_sys="cartesian")

        ####################
        # Governing equations
        ####################
        # for velocity_profile and thickness_convergence
        grad = mu * pybamm.grad(u)
        self.algebraic[u] = pybamm.div(grad) - P

        # for viscosity_profile
        self.variables["Shear stress [Pa]"] = mu * gamma

        # for analytical coating thickness - FBP: I changed units from mm to m please double check
        self.variables["Analytical coating thickness [m]"] = (
            -((-P * H_g + A_1) ** (1 / n + 2)) - (A_1) ** (1 / n + 2)
        ) / (U * P * (-1 / P * mu ** (1 / n)) * (1 / n + 1) * (1 / n + 2)) + A_2 * H_g

        ####################
        # Boundary conditions
        ####################
        # for velocity_profile and thickness_convergence
        self.boundary_conditions = {
            u: {"left": (U, "Dirichlet"), "right": (0, "Dirichlet")}
        }
        self.initial_conditions = {u: U}

        ##################
        # Output variables
        ##################
        self.variables.update(
            {
                "Velocity [m.s-1]": u,
                "Coating thickness [m]": pybamm.Integral(u, y) / U,
                "y [m]": y,
            }
        )

    @property
    def default_geometry(self):
        H_g = pybamm.Parameter("Coating gap [m]")
        y = self.variables["y [m]"]
        return {"coating": {y: {"min": pybamm.Scalar(0), "max": H_g}}}

    @property
    def default_var_pts(self):
        y = self.variables["y [m]"]
        return {y: 20}

    @property
    def default_submesh_types(self):
        return {"coating": pybamm.Uniform1DSubMesh}

    @property
    def default_spatial_methods(self):
        return {"coating": pybamm.FiniteVolume()}

    @property
    def default_solver(self):
        return pybamm.AlgebraicSolver()

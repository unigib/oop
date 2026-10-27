"""Interactive Tkinter application demonstrating object-oriented programming."""

from abc import ABC, abstractmethod
from pathlib import Path
import tkinter as tk
from tkinter import ttk


class Vehicle(ABC):
    """Abstract base class for vehicles."""

    vehicles_created = 0

    def __init__(self, make: str, model: str, mileage: int = 0) -> None:
        if not self.is_valid_mileage(mileage):
            raise ValueError("Mileage must be a non-negative integer.")

        self.make = make
        self.model = model
        self._mileage = mileage
        Vehicle.vehicles_created += 1

    @property
    def mileage(self) -> int:
        """Read-only access to the vehicle's mileage."""
        return self._mileage

    @staticmethod
    def is_valid_mileage(value: int) -> bool:
        """Validate mileage without needing a Vehicle instance."""
        return isinstance(value, int) and not isinstance(value, bool) and value >= 0

    @classmethod
    def from_dict(cls, details: dict[str, object]) -> "Vehicle":
        """Create the appropriate subclass from a dictionary."""
        return cls(
            str(details["make"]),
            str(details["model"]),
            int(details.get("mileage", 0)),
        )

    @abstractmethod
    def start(self) -> str:
        """Each concrete vehicle defines how it starts."""

    def __str__(self) -> str:
        return f"{self.make} {self.model} ({self.mileage:,} miles)"


class Car(Vehicle):
    """A conventional car, inheriting shared behavior from Vehicle."""

    def start(self) -> str:
        return f"{self}: the engine starts with a key."


class ElectricCar(Car):
    """A car with additional battery state and overridden behavior."""

    def __init__(
        self, make: str, model: str, mileage: int = 0, battery_percent: int = 100
    ) -> None:
        super().__init__(make, model, mileage)
        if not 0 <= battery_percent <= 100:
            raise ValueError("Battery percentage must be between 0 and 100.")
        self.battery_percent = battery_percent

    def start(self) -> str:
        return f"{self}: the electric motor starts silently."


class Garage:
    """A garage composes (owns and manages) a collection of vehicles."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._vehicles: list[Vehicle] = []

    def add(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def describe_vehicles(self) -> list[str]:
        return [vehicle.start() for vehicle in self._vehicles]


TOPICS = [
    {
        "title": "Classes & objects",
        "description": (
            "A class is a blueprint; an object is one instance built from it. "
            "Here, Car is a class and my_car is an object with its own make, "
            "model, and mileage."
        ),
        "code": (
            "my_car = Car(\"Toyota\", \"Corolla\", mileage=12000)\n"
            "print(my_car.model)  # Corolla\n"
            "print(my_car)        # Toyota Corolla (12,000 miles)"
        ),
        "demo": "objects",
    },
    {
        "title": "Encapsulation",
        "description": (
            "This complete, simplified Car class shows the usual structure: "
            "__init__ sets up each object, methods define its behavior, and "
            "the mileage property provides controlled read-only access to "
            "_mileage. A leading underscore is a Python convention, not a "
            "hard access restriction. In the app, Car inherits shared "
            "initialization and mileage behavior from Vehicle."
        ),
        "code": (
            "class Car:\n"
            "    def __init__(self, make, model, mileage=0):\n"
            "        self.make = make\n"
            "        self.model = model\n"
            "        self._mileage = mileage\n\n"
            "    @property\n"
            "    def mileage(self):\n"
            "        return self._mileage\n\n"
            "    def start(self):\n"
            "        return f\"{self.make} {self.model} starts.\"\n\n"
            "    def __str__(self):\n"
            "        return f\"{self.make} {self.model} ({self.mileage} miles)\"\n\n"
            "car = Car(\"Toyota\", \"Corolla\", 12000)\n"
            "print(car)          # Toyota Corolla (12000 miles)\n"
            "print(car.mileage)  # 12000"
        ),
        "demo": "encapsulation",
    },
    {
        "title": "Inheritance",
        "description": (
            "Inheritance lets a specialized class reuse and extend a base "
            "class. ElectricCar is a Car, and Car is a Vehicle. super() calls "
            "the parent initializer so shared state is set up once."
        ),
        "code": (
            "class ElectricCar(Car):\n"
            "    def __init__(self, make, model, battery_percent=100):\n"
            "        super().__init__(make, model)\n"
            "        self.battery_percent = battery_percent"
        ),
        "demo": "inheritance",
    },
    {
        "title": "Polymorphism",
        "description": (
            "Polymorphism means different object types can respond to the same "
            "method call in their own way. Garage can call start() on every "
            "Vehicle without checking whether it is a regular or electric car."
        ),
        "code": (
            "for vehicle in vehicles:\n"
            "    print(vehicle.start())\n\n"
            "# Car and ElectricCar each provide their own start()."
        ),
        "demo": "polymorphism",
    },
    {
        "title": "Abstraction",
        "description": (
            "An abstract base class defines a shared contract while leaving "
            "some details to subclasses. Vehicle requires start(); trying to "
            "instantiate Vehicle directly is not allowed."
        ),
        "code": (
            "class Vehicle(ABC):\n"
            "    @abstractmethod\n"
            "    def start(self):\n"
            "        ...\n\n"
            "# Every concrete Vehicle subclass must implement start()."
        ),
        "demo": "abstraction",
    },
    {
        "title": "Composition",
        "description": (
            "Composition builds a larger object from other objects. A Garage "
            "has a collection of Vehicle instances. This is a 'has-a' "
            "relationship, unlike inheritance's 'is-a' relationship."
        ),
        "code": (
            "garage = Garage(\"City Garage\")\n"
            "garage.add(Car(\"Toyota\", \"Corolla\"))\n"
            "garage.add(ElectricCar(\"Nissan\", \"Leaf\"))\n"
            "garage.describe_vehicles()"
        ),
        "demo": "composition",
    },
    {
        "title": "Class & static methods",
        "description": (
            "A class method receives the class (cls), so it can construct an "
            "instance from alternate input. A static method is a related "
            "utility that needs neither the class nor an instance."
        ),
        "code": (
            "car = Car.from_dict({\"make\": \"Honda\", \"model\": \"Civic\"})\n"
            "Vehicle.is_valid_mileage(120)  # True"
        ),
        "demo": "methods",
    },
    {
        "title": "Decorators",
        "description": (
            "A decorator uses @ syntax to wrap or configure a function. These "
            "examples show decorators used in this app: @property turns a "
            "method into an attribute-like read-only value, @staticmethod "
            "marks a utility that needs no instance or class, @classmethod "
            "receives the class as cls, and @abstractmethod marks a method "
            "that concrete subclasses must implement."
        ),
        "code": (
            "class Vehicle(ABC):\n"
            "    @property\n"
            "    def mileage(self):\n"
            "        return self._mileage\n\n"
            "    @staticmethod\n"
            "    def is_valid_mileage(value):\n"
            "        return value >= 0\n\n"
            "    @classmethod\n"
            "    def from_dict(cls, details):\n"
            "        return cls(details[\"make\"], details[\"model\"])\n\n"
            "    @abstractmethod\n"
            "    def start(self):\n"
            "        ..."
        ),
        "demo": "decorators",
    },
    {
        "title": "Special methods",
        "description": (
            "Special methods (often called dunder methods) let objects work "
            "with Python language features. Vehicle implements __str__ so "
            "print(vehicle) produces a useful description."
        ),
        "code": (
            "def __str__(self):\n"
            "    return f\"{self.make} {self.model} ({self.mileage:,} miles)\"\n\n"
            "print(car)"
        ),
        "demo": "special",
    },
]


class OOPDemoApp:
    """Build and control the Tkinter OOP learning interface."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Python OOP Explorer")
        self.root.geometry("940x690")
        self.root.minsize(760, 560)
        self._configure_style()
        self._build_interface()
        self.topic_list.selection_set(0)
        self.show_topic(0)

    def _configure_style(self) -> None:
        style = ttk.Style(self.root)
        if "vista" in style.theme_names():
            style.theme_use("vista")
        style.configure("Title.TLabel", font=("Segoe UI", 19, "bold"))
        style.configure("Subtitle.TLabel", font=("Segoe UI", 10))
        style.configure(
            "Institution.TLabel",
            font=("Segoe UI", 9, "bold"),
            foreground="#a6192e",
        )
        style.configure("Topic.TLabel", font=("Segoe UI", 13, "bold"))
        style.configure("Run.TButton", font=("Segoe UI", 10, "bold"), padding=7)

    def _build_interface(self) -> None:
        container = ttk.Frame(self.root, padding=18)
        container.pack(fill="both", expand=True)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(3, weight=1)

        header = ttk.Frame(container)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        self.logo_image = tk.PhotoImage(
            file=str(Path(__file__).with_name("logo.png"))
        ).subsample(3, 3)
        ttk.Label(header, image=self.logo_image).pack(side="left", padx=(0, 14))
        brand_text = ttk.Frame(header)
        brand_text.pack(side="left", anchor="center")
        ttk.Label(
            brand_text,
            text="UNIVERSITY OF GIBRALTAR",
            style="Institution.TLabel",
        ).pack(anchor="w", pady=(0, 2))
        ttk.Label(
            brand_text, text="Python OOP Explorer", style="Title.TLabel"
        ).pack(anchor="w")
        tk.Frame(container, height=3, background="#a6192e").grid(
            row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10)
        )
        ttk.Label(
            container,
            text="Explore object-oriented programming concepts with runnable examples.",
            style="Subtitle.TLabel",
        ).grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 14))

        sidebar = ttk.Frame(container)
        sidebar.grid(row=3, column=0, sticky="nsw", padx=(0, 18))
        ttk.Label(sidebar, text="CONCEPTS", font=("Segoe UI", 9, "bold")).pack(
            anchor="w", pady=(0, 7)
        )
        self.topic_list = tk.Listbox(
            sidebar,
            width=25,
            height=len(TOPICS),
            exportselection=False,
            activestyle="none",
            font=("Segoe UI", 10),
            relief="flat",
            highlightthickness=1,
        )
        for topic in TOPICS:
            self.topic_list.insert("end", topic["title"])
        self.topic_list.pack(fill="y", expand=True)
        self.topic_list.bind("<<ListboxSelect>>", self._on_topic_selected)

        content = ttk.Frame(container)
        content.grid(row=3, column=1, sticky="nsew")
        content.columnconfigure(0, weight=1)
        content.rowconfigure(3, weight=1)
        content.rowconfigure(6, weight=1)

        self.topic_title = ttk.Label(content, text="", style="Topic.TLabel")
        self.topic_title.grid(row=0, column=0, sticky="w")
        self.description = ttk.Label(
            content, text="", wraplength=620, justify="left"
        )
        self.description.grid(row=1, column=0, sticky="ew", pady=(6, 14))

        ttk.Label(content, text="Example", font=("Segoe UI", 9, "bold")).grid(
            row=2, column=0, sticky="w", pady=(0, 5)
        )
        self.code = tk.Text(
            content,
            height=14,
            wrap="none",
            font=("Consolas", 10),
            padx=10,
            pady=8,
            relief="flat",
            background="#f3f5f8",
            foreground="#233044",
        )
        self.code.grid(row=3, column=0, sticky="nsew")
        code_scrollbar = ttk.Scrollbar(
            content, orient="vertical", command=self.code.yview
        )
        code_scrollbar.grid(row=3, column=1, sticky="ns")
        self.code.configure(yscrollcommand=code_scrollbar.set, state="disabled")

        controls = ttk.Frame(content)
        controls.grid(row=4, column=0, sticky="ew", pady=(13, 7))
        ttk.Button(
            controls,
            text="Run this demo",
            style="Run.TButton",
            command=self.run_selected_demo,
        ).pack(side="left")
        ttk.Button(
            controls, text="Clear output", command=self.clear_output
        ).pack(side="left", padx=(8, 0))
        ttk.Label(content, text="Live output", font=("Segoe UI", 9, "bold")).grid(
            row=5, column=0, sticky="w", pady=(0, 5)
        )
        self.output = tk.Text(
            content,
            height=9,
            wrap="word",
            font=("Consolas", 10),
            padx=10,
            pady=8,
            relief="flat",
            background="#18212f",
            foreground="#e6edf5",
        )
        self.output.grid(row=6, column=0, sticky="nsew")
        self.output.configure(state="disabled")

    def _on_topic_selected(self, _event: tk.Event) -> None:
        selection = self.topic_list.curselection()
        if selection:
            self.show_topic(selection[0])

    def show_topic(self, index: int) -> None:
        topic = TOPICS[index]
        self.topic_title.configure(text=topic["title"])
        self.description.configure(text=topic["description"])
        self.code.configure(state="normal")
        self.code.delete("1.0", "end")
        self.code.insert("1.0", topic["code"])
        self.code.configure(state="disabled")
        self.clear_output()

    def _selected_topic(self) -> dict[str, str]:
        selection = self.topic_list.curselection()
        return TOPICS[selection[0] if selection else 0]

    def _write_output(self, message: str) -> None:
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", message.rstrip() + "\n")
        self.output.configure(state="disabled")

    def clear_output(self) -> None:
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

    def run_selected_demo(self) -> None:
        demo = self._selected_topic()["demo"]
        try:
            result = self._run_demo(demo)
        except (KeyError, TypeError, ValueError) as error:
            result = f"Demo error: {error}"
        self._write_output(result)

    def _run_demo(self, demo: str) -> str:
        if demo == "objects":
            my_car = Car("Toyota", "Corolla", mileage=12000)
            return f"Object created: {my_car}\nModel attribute: {my_car.model}"

        if demo == "encapsulation":
            car = Car("Honda", "Civic", mileage=8400)
            return (
                f"Read-only property value: car.mileage = {car.mileage}\n"
                "The property provides access without exposing a setter."
            )

        if demo == "inheritance":
            car = ElectricCar("Nissan", "Leaf", mileage=2500, battery_percent=82)
            return (
                f"ElectricCar is a Car: {isinstance(car, Car)}\n"
                f"Car is a Vehicle: {isinstance(car, Vehicle)}\n"
                f"Extra subclass attribute: battery = {car.battery_percent}%"
            )

        if demo == "polymorphism":
            vehicles: list[Vehicle] = [
                Car("Ford", "Focus"),
                ElectricCar("Tesla", "Model 3", battery_percent=95),
            ]
            return "The same start() call works for both types:\n" + "\n".join(
                f"• {vehicle.start()}" for vehicle in vehicles
            )

        if demo == "abstraction":
            try:
                Vehicle("Generic", "Vehicle")
            except TypeError as error:
                return (
                    "Vehicle is abstract, so it cannot be instantiated directly.\n"
                    f"Python says: {error}"
                )
            raise RuntimeError("The abstract Vehicle unexpectedly allowed creation.")

        if demo == "composition":
            garage = Garage("City Garage")
            garage.add(Car("Toyota", "Corolla", mileage=12000))
            garage.add(ElectricCar("Nissan", "Leaf", mileage=2500))
            return f"{garage.name} contains:\n" + "\n".join(
                f"• {description}" for description in garage.describe_vehicles()
            )

        if demo == "methods":
            car = Car.from_dict(
                {"make": "Honda", "model": "Civic", "mileage": 120}
            )
            return (
                f"Created via class method: {car}\n"
                f"Static validation of mileage 120: "
                f"{Vehicle.is_valid_mileage(120)}\n"
                f"Static validation of mileage -1: "
                f"{Vehicle.is_valid_mileage(-1)}"
            )

        if demo == "decorators":
            car = Car.from_dict(
                {"make": "Honda", "model": "Civic", "mileage": 120}
            )
            return (
                f"@property: car.mileage -> {car.mileage}\n"
                f"@staticmethod: valid mileage -> "
                f"{Vehicle.is_valid_mileage(car.mileage)}\n"
                f"@classmethod: from_dict created -> {car}\n"
                f"@abstractmethod: Vehicle requires -> "
                f"{', '.join(sorted(Vehicle.__abstractmethods__))}"
            )

        if demo == "special":
            car = Car("Mazda", "3", mileage=18000)
            return f"print(car) calls __str__:\n{car}"

        raise ValueError(f"Unknown demo: {demo}")


def main() -> None:
    root = tk.Tk()
    OOPDemoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

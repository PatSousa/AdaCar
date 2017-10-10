import React, { Component } from "react";
import logo from "./logo.svg";
import moment from "moment";
import "./App.css";

import Product from "./components/Product";
import Cart from "./components/Cart";

class App extends Component {
  constructor() {
    super();

    this.addToOrder = this.addToOrder.bind(this);
    this.finalizeOrder = this.finalizeOrder.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
  }

  state = {
    productList: [],
    orderProducts: [],
    order_id: null,
    showCart: false,
    orderDate: moment()
  };

  componentDidMount() {
    let productList = [];

    fetch("http://localhost:6543/")
      .then(blob => blob.json())
      .then(products => {
        productList.push(...products);
        this.setState({ productList });
      });
  }

  handleDateChange(date) {
    this.setState({
      orderDate: date
    });
  }

  addToOrder(part_id) {
    // take a copy of our state
    const order_id = this.state.order_id;
    const productList = [...this.state.productList];
    const orderProducts = [...this.state.orderProducts];
    // create order if it doesn't exist already
    if (!order_id) {
      fetch("http://localhost:6543/order", {
        method: "post",
        body: JSON.stringify({
          part_type_id: part_id
        })
      })
        .then(blob => blob.json())
        .then(order_id => {
          orderProducts.push(
            productList.filter(product => product.part_type_id === part_id)[0]
          );

          this.setState({
            order_id: order_id["order_id"],
            orderProducts: orderProducts
          });
        });
    } else {
      fetch(`http://localhost:6543/order/${order_id}`, {
        method: "post",
        body: JSON.stringify({
          part_type_id: part_id
        })
      })
        .then(blob => blob.json())
        .then(() => {
          orderProducts.push(
            productList.filter(product => product.part_type_id === part_id)[0]
          );
          this.setState({ orderProducts });
        });
    }
  }

  deleteFromOrder() {}

  finalizeOrder() {
    const order_id = this.state.order_id;
    const date = this.state.orderDate;
    fetch(`http://localhost:6543/order/${order_id}`, {
      method: "POST",
      body: JSON.stringify({
        delivery_date: date.format("DD/MM/YYYY HH:MM")
      })
    })
      .then(blob => blob.json())
      .then(() => {
        alert("order Completed");
      });
  }

  render() {
    const { productList } = this.state;

    return (
      <div className={`App ${this.state.showCart ? "showCart" : "hideCart"}`}>
        <nav className="navbar">
          <ul>
            <li className="logo">
              <a href="#">ADACar.</a>
            </li>
            <li className="cart">
              <a
                href="#"
                onClick={() =>
                  this.setState({ showCart: !this.state.showCart })}
              >
                Cart
              </a>
            </li>
          </ul>
        </nav>
        <ul className="partsList">
          {productList.map((product, index) => (
            <Product {...product} key={index} addToOrder={this.addToOrder} />
          ))}
        </ul>
        <Cart
          order={this.state.order}
          orderProducts={this.state.orderProducts}
          finalizeOrder={this.finalizeOrder}
          handleDateChange={this.handleDateChange}
          deleteFromOrder={this.deleteFromOrder}
          orderDate={this.state.orderDate}
        />
      </div>
    );
  }
}

export default App;

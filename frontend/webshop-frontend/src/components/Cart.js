import React, { Component } from "react";

import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";
import "./Cart.css";

class Cart extends Component {
  render() {
    const { orderProducts, orderDate } = this.props;

    return (
      <div className="YourCart">
        <h2>Your order</h2>
        <ul className="productsList">
          {orderProducts.map((product, index) => {
            return (
              <li key={index}>
                {product.part_type_name}
                <span>{product.part_type_value}€</span>
              </li>
            );
          })}
        </ul>
        <p>Select your delivery date:</p>
        <DatePicker
          selected={orderDate}
          onChange={e => this.props.handleDateChange(e)}
          showTimeSelect
          dateFormat="DD/MM/YYYY HH:MM"
        />
        <button onClick={() => this.props.finalizeOrder()}>
          Finalize Order
        </button>
      </div>
    );
  }
}

export default Cart;

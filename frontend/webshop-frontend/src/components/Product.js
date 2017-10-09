import React, { Component } from "react";
import "./Product.css";

class Product extends Component {
  render() {
    const {
      part_type_description,
      part_type_id,
      part_type_image_url,
      part_type_name,
      part_type_value
    } = this.props;

    return (
      <li>
        <p>{part_type_name}</p>
        <img alt="" src={part_type_image_url} />
        <p>{part_type_description}</p>
        <p>€ {part_type_value}</p>
        <button onClick={() => this.props.addToOrder(part_type_id)}>
          Add to Cart
        </button>
      </li>
    );
  }
}

export default Product;

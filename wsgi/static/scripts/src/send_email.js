import React from "react";

export default class SendEmail extends React.Component {
  constructor() {
    super();
    this._handleClick = this._handleClick.bind(this);

  }

  render() {
    return (
      <a onClick={this._handleClick} className="btn btn-cta-primary pull-right" href="#"
         target="_blank"><i className="fa fa-paper-plane"></i> Contact Me</a>
    )
  }

  _handleClick(event) {
    event.preventDefault();
    $.get('../api/v1.0/email/', function (data) {
      if (data.success) {
        window.location = `mailto:${data.mail_to}`;
      }
    })
  }
}

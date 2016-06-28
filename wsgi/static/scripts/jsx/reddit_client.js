/** @jsx React.DOM */

// the user is hardcoded for now
const USER_ID = 1;
const ENTRIES_PER_PAGE = 8;
var React = require('react');
var ReactDom = require('react-dom');

class ReadingList extends React.Component {
  constructor() {
    super();
    this.endpoint = '';
    this.state = {
      reading_list: null
    };
  }
  _fetch_reading_list() {
    if (!this.state.reading_list) {
      $.ajax({
        method: 'GET',
        url: this.endpoint,
        dataType: 'json',
        cache: false,
        success: (data) => {
          if (data.success === true) {
            this.setState({reading_list: data.reading_list});
          }
        },
        error: (xhr, status, err) => {
          console.log(this.props.url, status, err.toString());
        }
      });
    }
  }
  componentWillMount() {
    this._fetch_reading_list();
  }
  componentDidMount() {
    this._timer = setInterval(() => this._fetch_reading_list(), 10000);
  }
  componentWillUnmount() {
    clearInterval(this._timer);
  }
  render() {
    var reading_list;
    if (this.state.reading_list && this.state.reading_list.length) {
      reading_list = this.state.reading_list.map((item) => (<li className="list-group-item"
                                                                key={item.id}>{item.title}</li>));
      // reading_list = this.state.reading_list.map(
      //   function(item) {return (<li key={item.id}>{item.title}</li>)}  )
    }
    else {
      reading_list = [];
    }
    return (
      <div>
        <ul className="list-group">{reading_list}</ul>
      </div>
    );
  }
}

class ReadingListBooksCurrentlyReading extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/currently_reading/';
  }
}


class ReadingListBooksFinished extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/finished_reading/';
  }
}

class ReadingListBooksFinishedGeneral extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/finished_reading_general/';
  }
}


class ReadingListBooksToRead extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/to_read/';
  }
}

class SendEmail extends React.Component {
  render() {
    return (
      <a onClick={this._handleClick.bind(this)} className="btn btn-cta-primary pull-right" href="#" target="_blank"><i className="fa fa-paper-plane"></i> Contact Me</a>
    )
  }
  _handleClick() {
    $.get( '../api/v1.0/email/', function(data) {
      if (data.success) {
        window.location = `mailto:${data.mail_to}`;
      }
    })
  }
}

ReactDom.render(
  <SendEmail/>, document.getElementById('contact-me')
);


ReactDom.render(
  <ReadingListBooksFinished/>, document.getElementById('reading-list-books-finished')
);

ReactDom.render(
  <ReadingListBooksCurrentlyReading/>, document.getElementById('reading-list-books-currently-reading')
);

ReactDom.render(
  <ReadingListBooksFinishedGeneral/>, document.getElementById('reading-list-books-finished-general')
);

ReactDom.render(
  <ReadingListBooksToRead/>, document.getElementById('reading-list-books-to-read')
);


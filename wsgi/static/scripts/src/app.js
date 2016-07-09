import $ from "jquery";
import SendEmail from "./send_email";

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
      reading_list = this.state.reading_list.map((item) =>
        (<li className="list-group-item" key={item.id}>
          <div className="row">
            <div className="col-md-3 col-sm-3 col-xs-4">
              <img src={item.image_url} className="img-responsive" alt=''/>
            </div>
            <div className="col-md-9 col-sm-9 col-xs-8">
              <a href={item.url}> {item.title} </a>
            </div>
          </div>
        </li>));
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


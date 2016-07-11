import React, {Component, PropTypes} from "react";
import ReactDom from "react-dom";
import SendEmail from "./components/SendMail";
import ReadingListBooksFinished from "./components/ReadingListBooksFinished";
import ReadingListBooksCurrentlyReading from "./components/ReadingListBooksCurrentlyReading";
import ReadingListBooksFinishedGeneral from "./components/ReadingListBooksFinishedGeneral";
import ReadingListBooksToRead from "./components/ReadingListBooksToRead";

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


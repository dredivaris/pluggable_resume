import ReadingList from "./ReadingList";

export default class ReadingListBooksToRead extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/to_read/';
  }
}

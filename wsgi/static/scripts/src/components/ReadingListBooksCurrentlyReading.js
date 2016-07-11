import ReadingList from "./ReadingList";

export default class ReadingListBooksCurrentlyReading extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/currently_reading/';
  }
}

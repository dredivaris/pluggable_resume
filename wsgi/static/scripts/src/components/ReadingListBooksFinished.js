import ReadingList from "./ReadingList";

export default class ReadingListBooksFinished extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/finished_reading/';
  }
}

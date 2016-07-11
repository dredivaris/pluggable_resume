import ReadingList from "./ReadingList";

export default class ReadingListBooksFinishedGeneral extends ReadingList {
  constructor() {
    super();
    this.endpoint = '/api/v1.0/reading_list/finished_reading_general/';
  }
}

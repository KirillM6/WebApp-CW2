import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable()
export class WebService {
  constructor(public http: HttpClient) {
  }
  games_list: any;
  getSteamGames(page: number) {
    return this.http.get(
      'http://localhost:4200/api/v1.0/SteamGames?pn=' + page)
  }
  getGame(id: any) {
    return this.http.get(
      'http://localhost:4200/api/v1.0/steamgames,' + id);
  }
  getRating(id: any) {
    return this.http.get(
      'http://localhost:4200/api/v1.0/steamgames/' + id + '/Rating');
  }
}

import { Component } from '@angular/core';
import { WebService } from "./web.service";

@Component({
  selector: 'steamgames',
  templateUrl: './steamgames.component.css',
  styleUrls: ['./steamgames.component.ts']
})
export class SteamGamesComponent {

  constructor(public webService: WebService) {}

  games_list: any;
  page: number = 1;

  ngOnInit() {
    if (sessionStorage['page']) {
      this.page = Number(sessionStorage['page']);
    }
    this.games_list = this.webService.getSteamGames(this.page);
  }
  previousPage() {
    if (this.page > 1) {
      this.page = this.page - 1;
      sessionStorage['page'] = this.page;
      this.games_list = this.webService.getSteamGames(this.page);
    }
  }
  nextPage() {
    this.page = this.page + 1;
    sessionStorage['page'] = this.page;
    this.games_list = this.webService.getSteamGames(this.page)
  }

}




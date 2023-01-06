import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { SteamGamesComponent } from "./steamgames.component";
import { HttpClientModule } from "@angular/common/http";
import { WebService } from "./web.service";
import { RouterModule } from "@angular/router";
import { HomeComponent } from "./home.component";
import { GameComponent } from "./game.component"
import { ReactiveFormsModule } from "@angular/forms";
import { AuthModule } from '@auth/auth0-angular'

var routes: any = [{
  path: '',
  component: HomeComponent
  },
  {
    path: 'SteamGames',
    component: SteamGamesComponent
  },
  {
    path: 'SteamGames/:id',
    component: GameComponent
  }

];
@NgModule({
  declarations: [
    AppComponent, SteamGamesComponent, HomeComponent, GameComponent
  ],
  imports: [
    BrowserModule, HttpClientModule, RouterModule.forRoot(routes), ReactiveFormsModule, AuthModule.forRoot({domain: 'assignment2.uk.auth0.com', clientId:'p3UJdyp0MfaTifR7lHKG1B1vC2oPyGub'})
  ],
  providers: [WebService],
  bootstrap: [AppComponent]
})

export class AppModule {}


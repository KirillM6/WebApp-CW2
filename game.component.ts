import {Component} from '@angular/core';
import {WebService} from "./web.service";
import {ActivatedRoute} from "@angular/router";
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent {
  onSubmit () {
    console.log(this.ratingForm.value);
  }
  game_list: any;
  Rating: any = [];
  constructor(private webService: WebService,
              private route: ActivatedRoute,
              private formBuilder: FormBuilder) {}
  ngOnInit() {
    this.ratingForm = this.formBuilder.group({
      stars: 5
    });

    this.game_list = this.webService.getGame(this.route.snapshot.params['id']);
    const {id} = this.route.snapshot.params;
    this.Rating = this.webService.getRating(id)

  }
}

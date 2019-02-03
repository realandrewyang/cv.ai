import { Component, OnInit } from '@angular/core';
import { AngularFireStorage } from '@angular/fire/storage';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.scss']
})
export class UploadComponent implements OnInit {

  constructor(private storage: AngularFireStorage) { }

  ngOnInit() {
  }

  uploadFile(event) {
    const file = event.target.files[0];
    const filePath = file.name;
    const task = this.storage.upload(filePath, file);
  }

}

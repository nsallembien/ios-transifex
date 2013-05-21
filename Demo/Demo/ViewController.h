//
//  ViewController.h
//  Demo
//
//  Created by Nico Sallembien on 5/21/13.
//  Copyright (c) 2013 Transifex. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *localeLabel;
@property (copy, nonatomic) NSString *userLocale;

- (IBAction)changeLocale:(id)sender;

@end

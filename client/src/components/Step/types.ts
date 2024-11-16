import React from 'react';

export type StepProps = {
  title: string;
  complete: boolean;
} & React.PropsWithChildren;
